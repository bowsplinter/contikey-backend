from django.http import JsonResponse
from django.db import connection

# Create your views here.

## /new creates a new channel with posted data if delete flag is anything but "True", 
## else it deletes that specified channel from given userid
def new(request):
	#if not POST nothing will be done
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			article_id = request.POST['article_id']
			channel_id = request.POST['channel_id'] if request.POST['channel_id'] != 'Null' else None
			url = request.POST['url']
			caption = request.POST['caption'] if request.POST['caption'] != 'Null' else None
			preview_image = request.POST['preview_image'] if request.POST['preview_image'] != 'Null' else None
			preview_title = request.POST['preview_title'] if request.POST['preview_title'] != 'Null' else None
			preview_text = request.POST['preview_text'] if request.POST['preview_text'] != 'Null' else None
			shared_from_article_id = request.POST['shared_from_article_id'] if request.POST['shared_from_article_id'] != 'Null' else None
			delete_flag = request.POST['delete_flag'] if request.POST['delete_flag'] != 'Null' else False

			if delete_flag == 'True':
				cursor.execute('DELETE FROM article WHERE article_id = %s AND url = %s', [article_id,url])
			else:
				cursor.execute('INSERT INTO article(article_id,channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', [article_id,channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id])
			
			cursor.execute('SELECT * FROM article WHERE article_id = %s AND url = %s', [article_id,url])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'article':article_id, 'data':data})

def like(request):
	#if not POST nothing will be done
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			user_id = request.POST['user_id']
			article_id = request.POST['article_id']
			like_status = request.POST['like_status']

			if like_status != '1':
				cursor.execute('DELETE FROM user_likes_article WHERE article_id = %s AND user_id = %s', [article_id,user_id])
			else:
				cursor.execute('INSERT INTO user_likes_article(article_id,user_id,like_status) VALUES (%s,%s,%s)', [article_id,user_id,like_status])
			
			cursor.execute('SELECT * FROM user_likes_article WHERE article_id = %s AND user_id = %s', [article_id,user_id])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'article':article_id, 'data':data})


def comment(request):
	#if not POST nothing will be done
	if request.method == 'POST':
		with connection.cursor() as cursor:
			#TODO input validation
			user_id = request.POST['user_id']
			comment_id = request.POST['comment_id']
			comment_text = request.POST['comment_text']
			article_id = request.POST['article_id']
			delete_flag = request.POST['delete_flag'] if request.POST['delete_flag'] != 'Null' else False


			if delete_flag == 'True':
				cursor.execute('DELETE FROM comment WHERE comment_id = %s AND article_id = %s AND user_id = %s', [comment_id,article_id,user_id])
			else:
				cursor.execute('INSERT INTO comment(comment_id,article_id,user_id,comment_text) VALUES (%s,%s,%s,%s)', [comment_id,article_id,user_id,comment_text])
			
			cursor.execute('SELECT * FROM comment WHERE comment_id = %s AND article_id = %s AND user_id = %s', [comment_id,article_id,user_id])
			data = _fetchAll(cursor)

			return JsonResponse(status=200, data = {'article':article_id, 'data':data})

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]