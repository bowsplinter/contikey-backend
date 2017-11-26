from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','DELETE'])
def view(request, article_id):
	try:
		user_id = request.session['user_id']
	except:
		user_id = None

	if request.method == 'GET':
		with connection.cursor() as cursor:
			#Get article information
			cursor.execute("SELECT * FROM article WHERE article_id = %s", [article_id])
			data = _fetchAll(cursor)[0]

			#Get comments on article
			cursor.execute("SELECT * FROM comment WHERE article_id = %s", [article_id])
			data['comments'] = _fetchAll(cursor)

			#Update views on article
			cursor.execute("INSERT INTO view(user_id,article_id) VALUES (%s, %s)", [user_id, article_id])
			
			return Response({'article': data},status=status.HTTP_200_OK)
	elif request.method == 'DELETE':
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM article WHERE article_id = %s' , [article_id])
			return Response({}, status=status.HTTP_200_OK)

@api_view(['POST'])
def new(request):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			try:
				url = request.POST.get('url')
				channel_id = request.POST.get('channel_id')
				caption = request.POST.get('caption', None)
				preview_image = request.POST.get('preview_image',None)
				preview_title = request.POST.get('preview_title',None)
				preview_text = request.POST.get('preview_text',None)
				shared_from_article_id = request.POST.get('shared_from_article_id',None)
			except:
				return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)

			cursor.execute('INSERT INTO article(channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id) VALUES (%s,%s,%s,%s,%s,%s,%s)', [channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id])
			
			# cursor.execute('SELECT * FROM article HAVING created_at=(SELECT max(created_at) FROM article WHERE url = %s)', [url])
			# data = _fetchAll(cursor)
			return Response(data = {}, status = status.HTTP_201_CREATED)

@api_view(['POST','DELETE'])
def like(request, article_id):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			try:
				#user_id = request.POST.get('user_id')
				article_id = request.POST.get('article_id')
				#If record in table, then it is a like
				#like_status = request.POST['like_status'] 
			except:
				return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)

			cursor.execute('INSERT INTO user_likes_article(article_id,user_id,like_status) VALUES (%s,%s,%s)', [article_id,user_id,like_status])
			return Response(data = {}, status = status.HTTP_201_CREATED)

	elif request.method == 'DELETE':
		with connection.cursor() as cursor:
			cursor.execute('DELETE FROM user_likes_article WHERE article_id = %s AND user_id = %s', [article_id,user_id])
			return Response({}, status=status.HTTP_200_OK)

@api_view(['POST'])
def comment(request):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			#user_id = request.POST.get('user_id')
			comment_id = request.POST.get('comment_id')
			comment_text = request.POST.get('comment_text')
			article_id = request.POST.get('article_id')

			cursor.execute('INSERT INTO comment(comment_id,article_id,user_id,comment_text) VALUES (%s,%s,%s,%s)', [comment_id,article_id,user_id,comment_text])
			
			# cursor.execute('SELECT * FROM comment WHERE comment_id = %s AND article_id = %s AND user_id = %s', [comment_id,article_id,user_id])
			# data = _fetchAll(cursor)
			return Response({}, status=status.HTTP_200_OK)

@api_view(['GET'])
def feed(request):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	page = 1

	#To figure out how to take pages from settings.py
	items_per_page = 10
	offset = (page-1) * items_per_page
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM article WHERE channel_id IN(SELECT channel_id FROM user_follows_channel WHERE user_id = %s) ORDER BY created_at DESC LIMIT %s,%s', [user_id,offset,items_per_page])

		data = _fetchAll(cursor)

	return Response({'feed': data},status=status.HTTP_200_OK)

def _fetchAll(cursor):
  columns = [col[0] for col in cursor.description]
  rows = cursor.fetchall()
  return [dict(zip(columns, row)) for row in rows]