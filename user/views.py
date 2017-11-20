from django.http import JsonResponse
from django.db import connection

def profile(request, user_id = 'me'):
  if user_id == 'me':
    user_id = 1 #.should get user's user_id from session key

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM user WHERE user_id = %s", [user_id])
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
    return JsonResponse({'user': dict(zip(columns, row))})