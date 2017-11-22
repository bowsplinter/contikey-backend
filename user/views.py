from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from . import facebook as fb
from . import sql

@csrf_exempt
@api_view(['POST'])
def login(request):
    accessToken = request.POST.get('accessToken', None)
    if accessToken == None:
        return Response({'error': 'accessToken required'}, status=status.HTTP_400_BAD_REQUEST)

    facebook_id = fb.inspectUserToken(accessToken)
    if not facebook_id:
        return Response({'error': 'invalid accessToken'}, status=status.HTTP_401_UNAUTHORIZED)

    # check if user exists, else fetch fb profile and create user
    selectUser = sql.facebookid_get_user(facebook_id)
    if selectUser:
        newUser = False
        user_id = selectUser[0]['user_id']
    else:
        newUser = True
        u = fb.getUserInfo(accessToken)
        u['facebook_id'] = facebook_id
        user_id = sql.insert_user(u)
        # TODO: add user friends
    user = sql.userid_get_user(user_id)[0]

    request.session['user_id'] = user['user_id'] # store user_id in session data
    return Response({'user': user, 'new_user': newUser})

@csrf_exempt
@api_view(['POST'])
def logout(request):
    if request.session.session_key == None:
        return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)

    request.session.flush() # delete session from DB and remove user's session cookie
    return Response({'success': True})

@api_view(['GET'])
def user_detail(request, user_id = 'me'):
    if user_id == 'me':
        try: # get user's user_id from session key
            user_id = request.session['user_id']
        except:
            return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)

    user = sql.userid_get_user(user_id)
    if not user:
        return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'user': user[0]})

@api_view(['GET'])
def user_channels(request, user_id):
    user = sql.userid_get_user(user_id)
    if not user:
        return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    channels = sql.userid_get_channels(user_id)
    return Response({'user': user[0], 'data': channels})

def _fetchAll(cursor):
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]