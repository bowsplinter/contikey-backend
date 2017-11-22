from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from . import facebook as fb

@csrf_exempt
def login(request):
  if request.method != 'POST':
    return JsonResponse({'code': 400, 'error': 'request method not supported. use POST instead'})

  accessToken = request.POST.get('accessToken', None)
  if accessToken == None:
    return JsonResponse({'code': 400, 'error': 'accessToken required'})

  facebook_id = fb.inspectUserToken(accessToken)
  if not facebook_id:
    return JsonResponse({'code': 400, 'error': 'invalid accessToken'})

  # check if user exists, else fetch fb profile and create user
  with connection.cursor() as cursor:
    selectUser = cursor.execute("SELECT * FROM user WHERE facebook_id = %s", [facebook_id])
    if selectUser:
      newUser = False
    else:
      newUser = True
      u = fb.getUserInfo(accessToken)
      cursor.execute("INSERT INTO user (facebook_id, name, email, photo) VALUES (%s, %s, %s, %s)",
        [facebook_id, u['name'], u['email'], u['photo']])
      # TODO: add user friends
    cursor.execute("SELECT * FROM user WHERE facebook_id = %s", [facebook_id])
    user = _fetchAll(cursor)[0]

  request.session['user_id'] = user['user_id'] # store user_id in session data
  return JsonResponse({'code': 200, 'user': user, 'new_user': newUser})

@csrf_exempt
def logout(request):
  if request.method != 'POST':
    return JsonResponse({'code': 400, 'error': 'request method not supported. use POST instead'})
  if request.session.session_key == None:
    return JsonResponse({'code': 400, 'error': 'no existing session or session expired'})
  
  request.session.flush() # delete session from DB and remove user's session cookie
  return JsonResponse({'code': 200, 'success': True})

def profile(request, user_id = 'me'):
  if user_id == 'me':
    try: # get user's user_id from session key
      user_id = request.session['user_id']
    except:
      return JsonResponse({'code':400, 'error': 'no existing session or session expired'})

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM user WHERE user_id = %s", [user_id])
    user = _fetchAll(cursor)[0]
    return JsonResponse({'user': user})

def channels(request, user_id):
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM user WHERE user_id = %s", [user_id])
    user = _fetchAll(cursor)[0]
    cursor.execute("SELECT * FROM channel WHERE user_id = %s", [user_id])
    data = _fetchAll(cursor)
    return JsonResponse({'user': user, 'data': data})

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]