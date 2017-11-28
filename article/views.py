from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import sql
import metascrapy


class article_helper(APIView):
	"""
		get:
		Given an article_id from the url,
		this returns the Article info, comments on an article and inserts a new record into the views table(including null).

		delete:
		Given an article_id from the url,
		this attempts to delete the article_id.
		
		post:
		This attempts to get further information on the url using metascrapy,
		then create a new channel with said information and POST body under the given user
	"""
	def get(self,request,article_id):
		try:
			user_id = request.session['user_id']
		except:
			user_id = None

		data,status = sql.get_article(article_id, user_id)
		return Response(data,status)

	def delete(self, request, article_id):
		data, status = sql.delete_article(article_id)
		return Response(data, status)

	def post(self, request):
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

class article_liker(APIView):
	"""		
		post:
		Given an article_id from the url,
		this attempts to get the user_id from the session and add a user-likes-article record.

		delete:
		Given an article_id from the url,
		this attempts to get the user_id from the session and delete a user-likes-article record.
	"""
	def post(self,request,article_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		data, statusr = sql.create_like(article_id,user_id)
		return Response(data, statusr)

	def delete(self, request, article_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

		data, statusr = sql.delete_like(article_id,user_id)
		return Response(data, statusr)

class article_commenter(APIView):
	"""		
		post:
		Given an article_id from the url,
		this attempts to get the user_id from the session and comment to the article_id.
	"""
	def post(self, request, article_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

		with connection.cursor() as cursor:
			comment_text = request.POST.get('comment_text')
			data, status = sql.create_comment(article_id,user_id,comment_text)

			return Response(data, status)

class article_feeder(APIView):
	"""		
		get:
		This attempts to get the user_id from the session and get the most recent articles from user_id's followed channels.

		#TODO: Follow proper pagination from REST framework
	"""
	def get(self, request):
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
