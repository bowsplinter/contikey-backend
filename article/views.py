import metascrapy
from django.http import JsonResponse
from django.db import connection
from . import sql
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','DELETE'])
def view(request, article_id):
	if request.method == 'GET':
		try:
			user_id = request.session['user_id']
		except:
			user_id = None

		data,status = sql.get_article(article_id, user_id)
		return Response(data,status)

	elif request.method == 'DELETE':
		data, status = sql.delete_article(article_id)
		return Response(data, status)

@api_view(['POST'])
def new(request):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			try:
				url = request.POST.get('url')
				if "http://" not in url:
					url = "http://" + url
				channel_id = request.POST.get('channel_id')
				caption = request.POST.get('caption', None)

				scraper = metascrapy.Metadata()
				scraper.scrape(url)

				preview_image = scraper.image #request.POST.get('preview_image',None)
				preview_title = scraper.title #request.POST.get('preview_title',None)
				preview_text = scraper.description #request.POST.get('preview_text',None)
				shared_from_article_id = request.POST.get('shared_from_article_id',None)
			except:
				return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)

			data, statusr = sql.create_article(channel_id,url,caption,preview_image,preview_title,preview_text,shared_from_article_id) 
			return Response(data, statusr)

@api_view(['POST','DELETE'])
def like(request, article_id):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		data, statusr = sql.create_like(article_id,user_id)
		return Response(data, statusr)

	elif request.method == 'DELETE':
		data, statusr = sql.delete_like(article_id,user_id)
		return Response(data, statusr)

@api_view(['POST'])
def comment(request, article_id):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			comment_text = request.POST.get('comment_text')
			data, status = sql.create_comment(article_id,user_id,comment_text)

			return Response(data, status)

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

	data = sql.get_user_feed(user_id, offset, items_per_page)
	return Response({'feed': data},status=status.HTTP_200_OK)
