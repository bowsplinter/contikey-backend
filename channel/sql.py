from functions import dictfetchall
from django.db import connection
from rest_framework import status

def get_user_explore(user_id,limit):
	with connection.cursor() as cursor:
		cursor.execute('SELECT channel_id FROM channel_tags WHERE tag_id=(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT %s', [user_id, user_id, limit])
		return dictfetchall(cursor)

	#User's followed tags
	#SELECT tag_id FROM user_follows_tag WHERE user_id = %s
	#SELECT channel_id FROM channel_tags ORDER BY rand() LIMIT 5

	#Needs a faster command
	#SELECT channel_id FROM channel_tags WHERE tag_id=(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT 5

def get_follow(user_id,channel_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO user_follows_channel (user_id, channel_id) VALUES (%s,%s)', [user_id,channel_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_201_CREATED

def delete_follow(user_id,channel_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM user_follows_channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_200_OK

def get_channel(channel_id):
	with connection.cursor() as cursor:
		try:
			#Channel table info
			cursor.execute("SELECT * FROM channel WHERE channel_id = %s", [channel_id])
			data = dictfetchall(cursor)[0]

			#Channel_tags table (retrive tags associated with channel)
			cursor.execute("SELECT * FROM channel_tags WHERE channel_id = %s", [channel_id])
			data['tags'] = _combineTags(dictfetchall(cursor))

			#user_follows_channel table (retrieve COUNT(user) following channel) 
			cursor.execute("SELECT COUNT(DISTINCT user_id) FROM user_follows_channel WHERE channel_id= %s" , [channel_id])
			data['number_of_follows'] = cursor.fetchone()[0]

		except Exception as e:
			return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
		return {'channel':data}, status.HTTP_200_OK	

def create_channel(user_id,title,description):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO channel (user_id,title,description) VALUES (%s,%s,%s)', [user_id,title,description])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_201_CREATED

def delete_channel(user_id,channel_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM channel WHERE user_id = %s AND channel_id = %s', [user_id,channel_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_200_OK

def _combineTags(data):
	tags = []
	for key in data:
		tags.append(key['tag_id'])
	return tags