from functions import dictfetchall
from django.db import connection
from rest_framework import status


def get_user_feed(user_id, offset, items_per_page):
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM article WHERE channel_id IN(SELECT channel_id FROM user_follows_channel WHERE user_id = %s) ORDER BY created_at DESC LIMIT %s,%s', [user_id,offset,items_per_page])
		return dictfetchall(cursor)

def get_article(article_id, user_id = None):
	with connection.cursor() as cursor:
		try:
				#Get article information
				cursor.execute("SELECT * FROM article WHERE article_id = %s", [article_id])
				data = dictfetchall(cursor)[0]

				#Get comments on article
				cursor.execute("SELECT * FROM comment WHERE article_id = %s", [article_id])
				
				data['comments'] = dictfetchall(cursor)
		except Exception as e:
			#Not rolling back changes yet
			return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
		
		#Update views on article
		cursor.execute("INSERT INTO view(user_id,article_id) VALUES (%s, %s)", [user_id, article_id])
	return {'article':data}, status.HTTP_200_OK		

def create_article(channel_id,url,caption = None,preview_image = None,preview_title = None,preview_text = None,shared_from_article_id = None):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO article(channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id) VALUES (%s,%s,%s,%s,%s,%s,%s)', [channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_201_CREATED

def delete_article(article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM article WHERE article_id = %s' , [article_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_200_OK	

def create_like(article_id,user_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO user_likes_article(article_id,user_id) VALUES (%s,%s)', [article_id,user_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_201_CREATED	

def delete_like(article_id,user_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM user_likes_article WHERE article_id = %s AND user_id = %s', [article_id,user_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_200_OK	

def create_comment(article_id,user_id,comment_text):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO comment(article_id,user_id,comment_text) VALUES (%s,%s,%s)', [article_id,user_id,comment_text])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_201_CREATED		