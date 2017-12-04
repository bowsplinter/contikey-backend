from functions import dictfetchall, listfetchall
from django.db import connection
from rest_framework import status
import functionssql as fs

def get_user_feed(user_id):
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM article WHERE channel_id IN(SELECT channel_id FROM user_follows_channel WHERE user_id = %s) ORDER BY created_at DESC', [user_id])
		data = dictfetchall(cursor)
		for article in data:
			article['user'] = get_article_poster(article['article_id'])[0]
			article['channel'] = get_article_channel(article['channel_id'])[0]
		return data

def get_nologin_feed():
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM article ORDER BY created_at DESC')
		data = dictfetchall(cursor)
		for article in data:
			article['user'] = get_article_poster(article['article_id'])[0]
			article['channel'] = get_article_channel(article['channel_id'])[0]
		return data	

#Get article information
def get_article(article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM article WHERE article_id = %s", [article_id])
			data = dictfetchall(cursor)[0]
	except IndexError:
		return {'error':'article not found'}, HTTP_404_NOT_FOUND
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

#Get article information for a list or tuple of articles
def get_articles(article_ids):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM article WHERE article_id IN %s", [tuple(article_ids)])
			data = dictfetchall(cursor)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

def get_top_monthly_articles():
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT article_id FROM user_likes_article WHERE TIMESTAMPDIFF(DAY, created_at, NOW()) < 31 GROUP BY article_id ORDER BY count(*) DESC LIMIT 10")
			article_ids = listfetchall(cursor)
			data = get_articles(article_ids)[0]
			data = fs.articlelist_get_channel(data)
			data = fs.articlelist_get_user(data)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

#Get article's poster information
def get_article_poster(article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT user.* FROM user JOIN channel USING(user_id) JOIN article USING(channel_id) WHERE article_id = %s", [article_id])
			data = dictfetchall(cursor)[0]
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK	

#Get article's poster and channel information
def get_article_channel(article_id):
	try:
		with connection.cursor() as cursor:
			print("article_id: "+str(article_id))
			cursor.execute("SELECT channel.* FROM channel JOIN article USING(channel_id) WHERE article_id = %s", [article_id])
			data = dictfetchall(cursor)[0]
			print(data)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK	

#Get comments (and the user who posted them) on article
def get_article_comments(article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM comment JOIN user USING(user_id) WHERE article_id = %s", [article_id])
			data = dictfetchall(cursor)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

#Get if current user liked article
def get_user_liked_article(user_id, article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT exists(SELECT 1 FROM user_likes_article WHERE user_id = %s AND article_id = %s) liked",
				[user_id, article_id])
			data = dictfetchall(cursor)[0]
			res = True if data['liked'] is 1 else False;
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return res, status.HTTP_200_OK

#Get number of likes on article
def get_article_likes(article_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT count(distinct user_id) likes FROM user_likes_article WHERE article_id = %s", [article_id])
			data = dictfetchall(cursor)[0]['likes']
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

#Update views on article
def create_view(article_id,user_id = None):
	try:
		with connection.cursor() as cursor:
			cursor.execute("INSERT INTO view(user_id,article_id) VALUES (%s, %s)", [user_id, article_id])
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return {}, status.HTTP_200_OK

def create_article(channel_id,url,caption = None,preview_image = None,preview_title = None,preview_text = None, num_words=None, shared_from_article_id = None):
	try:
		with connection.cursor() as cursor:
			cursor.execute('INSERT INTO article(channel_id,url,caption,preview_image,preview_title,preview_text,num_words, shared_from_article_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', [channel_id,url,caption,preview_image,preview_title,preview_text,num_words,shared_from_article_id])
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
			data, get_status = created_get_comment(article_id,user_id)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_201_CREATED

#This to be used by create comment to immediately get created comment
#Look into last_inserted_id() why it doesnt work?
def create_get_comment(article_id, user_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('SELECT * FROM comment WHERE article_id = %s AND user_id = %s HAVING max(created_at)', [article_id,user_id])
			data = dictfetchall(cursor)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK

def get_comment(comment_id):
	try:
		with connection.cursor() as cursor:
			cursor.execute('SELECT * FROM comment WHERE comment_id = %s', [comment_id])
			data = dictfetchall(cursor)
	except Exception as e:
		return {'errorType':str(type(e)), 'errorArgs':e.args}, status.HTTP_500_INTERNAL_SERVER_ERROR
	return data, status.HTTP_200_OK
