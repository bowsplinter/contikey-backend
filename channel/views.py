from django.http import JsonResponse
from django.db import connection

# Create your views here.
def channel(request, channel_id = 1):
	#user_id = request.session['user_id']
	if request.method == 'GET':
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
	elif request.method == 'DELETE':
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			return JsonResponse({'code':'200'})

## /new creates a new channel with posted data if delete flag is anything but "True", 
## else it deletes that specified channel from given userid
def new(request, user_id = 1):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			try:
				title = request.POST['title']
				description = request.POST['description']
			except:
				return JsonResponse(status=400, data = {'code':'400','error':'missing or invalid POST body'})
			cursor.execute('INSERT INTO channel (user_id,title,description) VALUES (%s,%s,%s)', [user_id,title,description])
			
			cursor.execute('SELECT * FROM channel HAVING created_at=(SELECT max(created_at) FROM channel WHERE user_id = %s)', [user_id])
			data = _fetchAll(cursor)

			return JsonResponse({'code':'201', 'data':data})			

## /follow makes thie given user follow the given channel if delete flag is anything but "True", 
## else it deletes that followed channel from given userid
def follow(request, channel_id = 1):
	#user_id = request.session['user_id']
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			#channel_id = request.POST['channel_id']
			user_id = request.POST['user_id']
			cursor.execute('INSERT INTO user_follows_channel (user_id, channel_id) VALUES (%s,%s)', [user_id,channel_id])
			
			cursor.execute('SELECT * FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			data = _fetchAll(cursor)

			return JsonResponse({'code':'200','data':data})
	elif request.method == 'DELETE':
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])

			return JsonResponse({'code':'200'})			

def explore(request):
	return JsonResponse(status=501, data={'code':'501','error':'not implemented'})

def _combineTags(data):
	tags = []
	for key in data:
		tags.append(key['tag_id'])
	return tags

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]