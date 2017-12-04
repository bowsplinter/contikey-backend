from django.http import JsonResponse
from django.db import connection
from django.core.paginator import Paginator
from rest_framework import status, serializers, pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.utils.urls import replace_query_param
from . import sql
import metascrapy


class article_helper(APIView):
	parser_classes = (JSONParser,MultiPartParser)
	"""
		get:
		Given an article_id from the url,
		this returns the Article info,
		comments on an article and,
		likes on an article,
		if the current user liked the article,
		the user and channel this article belongs to,
		and inserts a new record into the views table(including null).

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

		#[0]'s to ignore status response from sql commands
		data,status = sql.get_article(article_id)
		data['comments'] = sql.get_article_comments(article_id)[0]
		data['likes'] = sql.get_article_likes(article_id)[0]
		data['user_channel'] = sql.get_article_poster_channel(article_id)[0]
		if user_id != None:
			data['liked'] = sql.get_user_liked_article(user_id, article_id)[0]
		sql.get_article_new_view(article_id,user_id)
		return Response(data,status)

	def delete(self, request, article_id):
		data, status = sql.delete_article(article_id)
		return Response(data, status)

	def post(self, request):
		with connection.cursor() as cursor:
			try:
				url = request.data.get('url')
				channel_id = request.data.get('channel_id')
				caption = request.data.get('caption', None)
				shared_from_article_id = request.data.get('shared_from_article_id',None)
			except Exception:
				return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)
			if "http://" not in url:
				url = "http://" + url
			scraper = metascrapy.Metadata()
			scraper.scrape(url)
			preview_image = scraper.image #request.POST.get('preview_image',None)
			preview_title = scraper.title #request.POST.get('preview_title',None)
			preview_text = scraper.description #request.POST.get('preview_text',None)
            num_words = scraper.num_words

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
			comment_text = request.data.get('comment_text')
			data, status = sql.create_comment(article_id,user_id,comment_text)
			return Response(data, status)

class article_feeder(APIView):
	"""
		get:
		This attempts to get the user_id from the session and get the most recent articles from user_id's followed channels.
		If the user is not logged in this returns a "most recent" feed from all possible channels.
	"""
	def get(self, request):
		try:
			user_id = request.session['user_id']
			queryset = sql.get_user_feed(user_id)
			paginator = article_paginator()
			result_page = paginator.paginate_queryset(queryset, request)
			serializer = article_serializer(result_page, many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		except:
			queryset = sql.get_nologin_feed()
			paginator = article_paginator()
			result_page = paginator.paginate_queryset(queryset, request)
			serializer = article_serializer(result_page, many=True)
			return Response({'feed': serializer.data },status=status.HTTP_200_OK)

class article_paginator(pagination.PageNumberPagination):
	def get_paginated_response(self, data):
		return Response({'count': self.page.paginator.count,'next':self.get_next_link(),'previous':self.get_previous_link(),'data':data})

	def get_next_link(self):
		if not self.page.has_next():
			return None
		page_number = self.page.next_page_number()
		return replace_query_param('', self.page_query_param, page_number)

	def get_previous_link(self):
		if not self.page.has_previous():
			return None
		page_number = self.page.previous_page_number()
		return replace_query_param('', self.page_query_param, page_number)

class article_serializer(serializers.Serializer):
	article_id = serializers.IntegerField()
	#These few should switch to 128 and 512 to be more efficient, Padded anyway.
	url = serializers.CharField(max_length=500)
	caption = serializers.CharField(max_length=500)
	preview_image = serializers.CharField(max_length=500)
	preview_title = serializers.CharField(max_length=100)
	preview_text = serializers.CharField(max_length=500)
	channel_id = serializers.IntegerField()
	shared_from_article_id = serializers.IntegerField()
	created_at = serializers.DateTimeField()
	user_info = serializers.DictField()

class article_data():
	def __init__(self,article_id,url,caption,preview_image,preview_title,preview_text,channel_id,shared_from_article_id,created_at,user_info):
		self.article_id = article_id
		self.url = url
		self.caption = caption
		self.preview_image = preview_image
		self.preview_title = preview_title
		self.preview_text = preview_text
		self.channel_id = channel_id
		self.shared_from_article_id = shared_from_article_id
		self.created_at = created_at
		self.user_info = user_info
