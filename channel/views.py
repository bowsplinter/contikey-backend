from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','DELETE'])
def channel(request, channel_id):
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

			return Response({'data': data},status=status.HTTP_200_OK)
	elif request.method == 'DELETE':
		try:
			user_id = request.session['user_id']
		except:
			user_id = None

		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			return Response({}, status=status.HTTP_200_OK)

@api_view(['POST'])
def new(request, user_id):
	if request.method == 'POST':
			try:
				title = request.POST.get('title')
				description = request.POST.get('description')
			except:
				return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)			
			cursor.execute('INSERT INTO channel (user_id,title,description) VALUES (%s,%s,%s)', [user_id,title,description])
			# cursor.execute('SELECT * FROM channel HAVING created_at=(SELECT max(created_at) FROM channel WHERE user_id = %s)', [user_id])
			# data = _fetchAll(cursor)
			Response({},status=status.HTTP_201_CREATED)		

@api_view(['POST','DELETE'])
def follow(request, channel_id):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			#channel_id = request.POST['channel_id']
			#user_id = request.POST['user_id']
			cursor.execute('INSERT INTO user_follows_channel (user_id, channel_id) VALUES (%s,%s)', [user_id,channel_id])
			
			# cursor.execute('SELECT * FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
			# data = _fetchAll(cursor)

			return Response({}, status=status.HTTP_200_OK)
	elif request.method == 'DELETE':
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])

			return Response({}, status=status.HTTP_200_OK)		

# Will need user_id likely
@api_view(['GET'])
def explore(request):
	try:
		user_id = request.session['user_id']
	except:
		#user_id = None
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		limit = 5;
		with connection.cursor() as cursor:
			cursor.execute('SELECT channel_id FROM channel_tags WHERE tag_id=(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT %s', [user_id, user_id, limit])
			data = _fetchAll(cursor)

	#User's followed tags
	#SELECT tag_id FROM user_follows_tag WHERE user_id = %s
	#SELECT channel_id FROM channel_tags ORDER BY rand() LIMIT 5

	#Needs a faster command
	#SELECT channel_id FROM channel_tags WHERE tag_id=(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT 5

	return Response({'channels': data},status=status.HTTP_200_OK)

def _combineTags(data):
	tags = []
	for key in data:
		tags.append(key['tag_id'])
	return tags

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]