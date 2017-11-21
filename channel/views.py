from django.http import JsonResponse
from django.db import connection

# Create your views here.
def channel(request, channel_id = 'None'):
	if channel_id == 'None':
		channel_id = 1
	with connection.cursor() as cursor:
		#Channel table info
	    cursor.execute("SELECT * FROM channel WHERE channel_id = %s", [channel_id])
	    data = _fetchAll(cursor)[0]
	    #Channel_tags table (retrive tags associated with channel)
	    cursor.execute("SELECT * FROM channel_tags WHERE channel_id = %s", [channel_id])
	    data['tags'] = _combineTags(_fetchAll(cursor))
	    #user_follows_channel table (retrieve COUNT(user) following channel) 
	    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM user_follows_channel WHERE channel_id= %s" , [channel_id])
	    data['number_of_follows'] = cursor.fetchone()[0]
	    return JsonResponse({'data': data})

## /new creates a new channel with posted data if delete flag is anything but "True", 
## else it deletes that specified channel from given userid
def new(request, user_id = 'None'):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			try:
				user_id = request.POST['user_id']
				title = request.POST['title']
				description = request.POST['description']
			except:
				return JsonResponse(status=400, data = {'error':'missing or invalid POST body'})
			#cursor.execute('DELETE FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			cursor.execute('INSERT INTO channel (user_id,title,description) VALUES (%s,%s,%s)', [user_id,title,description])
			
			cursor.execute('SELECT * FROM channel HAVING created_at=(SELECT max(created_at) FROM channel WHERE user_id = %s)', [user_id])
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
			delete_flag = request.POST['delete_flag']

			if delete_flag == 'True':
				cursor.execute('DELETE FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			else:
				cursor.execute('INSERT INTO user_follows_channel (user_id, channel_id) VALUES (%s,%s)', [user_id,channel_id])
			
			cursor.execute('SELECT * FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'user':user_id, 'data':data})

def _combineTags(data):
	tags = []
	for key in data:
		tags.append(key['tag_id'])
	return tags

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]