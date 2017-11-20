from django.http import JsonResponse
from django.db import connection

def profile(request, user_id = 'me'):
  if user_id == 'me':
    user_id = 1 #.should get user's user_id from session key

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