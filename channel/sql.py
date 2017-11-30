from functions import dictfetchall
from django.db import connection
from rest_framework import status

def get_user_explore(user_id,limit):
	with connection.cursor() as cursor:
		cursor.execute('SELECT DISTINCT ct.* FROM channel_tags ct LEFT JOIN user_follows_channel f ON ct.channel_id = f.channel_id WHERE ct.tag_id IN(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND f.user_id != %s ORDER BY rand() LIMIT = %s', [user_id, user_id, limit])

		#cursor.execute('SELECT DISTINCT channel_id FROM channel_tags WHERE tag_id IN(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT %s', [user_id, user_id, limit])
		return dictfetchall(cursor)

	#User's followed tags
	#SELECT tag_id FROM user_follows_tag WHERE user_id = %s
	#SELECT channel_id FROM channel_tags ORDER BY rand() LIMIT 5

	#Needs a faster command
	#SELECT channel_id FROM channel_tags WHERE tag_id=(SELECT tag_id FROM user_follows_tag WHERE user_id = %s) AND NOT EXISTS (SELECT channel_id from user_follows_channel WHERE user_id = %s) ORDER BY rand() LIMIT 5

def get_nologin_explore():
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM channel ORDER BY rand()')
		return dictfetchall(cursor)

def new_follow(user_id,channel_id):
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

#To move to article.sql?
def get_channel_articles(channel_id):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT * FROM article WHERE channel_id = %s", [channel_id])
			data = dictfetchall(cursor)
		except Exception as e:
			return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
		return {'articles':data}, status.HTTP_200_OK				

#Returns the last inserted channel_id (which should be the created one, since last_insert_id goes by connection), for auto-following of created channel
def create_channel(user_id,title,description,tags):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO channel (user_id,title,description) VALUES (%s,%s,%s)', [user_id,title,description])
			#print("channel insert success")
			cursor.execute('SELECT last_insert_id()')
			last_insert = str(dictfetchall(cursor)[0]['last_insert_id()'])
			#print('last insert obtained: '+last_insert)
			#Expect tags as list of tag_ids
			tags_insert_str = 'INSERT INTO channel_tags(channel_id, tag_id) VALUES '
			for tag in tags:
				tags_insert_str += '('+last_insert+','+tag+'),'
			#print(tags_insert_str[:-1])
			cursor.execute(tags_insert_str[:-1])
			#print('channel_tags insert success')
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return last_insert, status.HTTP_201_CREATED

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