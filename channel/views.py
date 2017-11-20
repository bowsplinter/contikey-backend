from django.http import JsonResponse
from django.db import connection

# Create your views here.
def channel(request, channel_id = 'None'):
	if channel_id == 'None':
		channel_id = 1
	with connection.cursor() as cursor:
	    cursor.execute("SELECT * FROM channel WHERE channel_id = %s", [channel_id])
	    data = _fetchAll(cursor)
	    return JsonResponse({'data': data})

## /new creates a new channel with posted data if delete flag is anything but "True", 
## else it deletes that specified channel from given userid
def new(request):
	#if not POST nothing will be done
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			channel_id = request.POST['channel_id']
			user_id = request.POST['user_id']
			title = request.POST['title']
			description = request.POST['description']
			delete_flag = request.POST['delete_flag']

			if delete_flag == 'True':
				cursor.execute('DELETE FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			else:
				cursor.execute('INSERT INTO channel (channel_id,user_id,title,description) VALUES (%s,%s,%s,%s)', [channel_id,user_id,title,description])
			
			cursor.execute('SELECT * FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'user':user_id, 'data':data})


## /follow makes thie given user follow the given channel if delete flag is anything but "True", 
## else it deletes that followed channel from given userid
def follow(request):
	#if not POST nothing will be done
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			channel_id = request.POST['channel_id']
			user_id = request.POST['user_id']
			#target_id = request.POST['target_id']
			delete_flag = request.POST['delete_flag']

			if delete_flag == 'True':
				cursor.execute('DELETE FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			else:
				cursor.execute('INSERT INTO user_follows_channel (user_id, channel_id) VALUES (%s,%s)', [user_id,channel_id])
			
			cursor.execute('SELECT * FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'user':user_id, 'data':data})


def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]