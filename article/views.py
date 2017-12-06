from django.http import JsonResponse
from django.db import connection
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from rest_framework import status, serializers, pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.utils.urls import replace_query_param
from . import sql
import metascrapy


class article_helper(APIView):
	"""
	get:
	Given an article_id from the url,
	this returns the Article info, comments, likes,
	if the current user liked the article, 
	the user and channel this article belongs to,
	and inserts a new record into the views table(including nulluser).

	delete:
	Given an article_id from the url,
	this attempts to delete the article_id.	

	post:
	This attempts to get further information on the url using metascrapy,
	then create a new channel with said information and POST body under the given logged in user
	"""
	parser_classes = (JSONParser,MultiPartParser)

	def get(self,request,article_id):
		try:
			user_id = request.session['user_id']
		except:
			user_id = None

		try:
			with connection.cursor() as cursor:
				data = sql.get_article(article_id, cursor)
				data['comments'] = sql.get_article_comments(article_id)
				data['likes'] = sql.get_article_likes(article_id)
				data['user'] = sql.get_article_poster(article_id)
				data['channel'] = sql.get_article_channel(article_id)
				if user_id != None:
					data['liked'] = sql.get_user_liked_article(user_id, article_id)
				sql.create_view(article_id,user_id)

		except IndexError:
			return Response({'message':'article not found'}, status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			return Response({'errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_200_OK)

	def delete(self, request, article_id):
		try:
			data = sql.delete_article(article_id)
		except Exception as e:
			return Response({'errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_200_OK)

	def post(self, request):
		try:
			url = request.data.get('url')
			channel_id = request.data.get('channel_id')
			caption = request.data.get('caption', None)
			num_words = request.data.get('num_words', None)
			shared_from_article_id = request.data.get('shared_from_article_id',None)
		except Exception:
			return Response({'message':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			if "http://" not in url:
				url = "http://" + url
			scraper = metascrapy.Metadata()
			scraper.scrape(url)
			preview_image = scraper.image #request.POST.get('preview_image',None)
			preview_title = scraper.title.encode('utf-8') #request.POST.get('preview_title',None)
			preview_text = scraper.description.encode('utf-8') #request.POST.get('preview_text',None)
		except Exception as e:
			return Response({'message':'invalid url'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			data = sql.create_article(channel_id,url,caption,preview_image,preview_title,preview_text,num_words,shared_from_article_id) 
		except Exception as e:
			return Response({'message':'failed to create record'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_201_CREATED)

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
			return Response({'message':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			data = sql.create_like(article_id,user_id)
		except IntegrityError as ie:
			return Response({'message':'Cannot Like a Liked article'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_201_CREATED)

	def delete(self, request, article_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'message':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			data = sql.delete_like(article_id,user_id)
		except Exception as e:
			return Response({'errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_200_OK)

class article_commenter(APIView):
	"""
		post:
		Given an article_id from the url,
		this attempts to get the user_id from the session and add a comment to the article_id.
	"""
	def post(self, request, article_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'message':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

		try:
			comment_text = request.data.get('comment_text')
			data = sql.create_comment(article_id,user_id,comment_text)
		except Exception as e:
			return Response({'errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(data, status=status.HTTP_201_CREATED)

class article_explorer(APIView):
	"""
		get:
		Returns the top 10 most liked articles in the last month
	"""
	def get(self, request):
		data = sql.get_top_monthly_articles()
		return Response({'data':data}, status=status.HTTP_200_OK)
		
class article_feeder(APIView):
	"""
		get:
		Attempts to get the user_id from the session and get the most recent articles from user_id's followed channels.
		If the user is not/cannot be logged in this returns a "most recent" feed from all possible channels.
	"""
	def get(self, request):
		try:
			user_id = request.session['user_id']
			queryset = sql.get_user_feed(user_id)
		except:
			queryset = sql.get_nologin_feed()
			
		paginator = article_paginator()
		result_page = paginator.paginate_queryset(queryset, request)
		serializer = article_serializer(result_page, many=True)
		return Response({'feed':serializer.data},status=status.HTTP_200_OK)

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
	user = serializers.DictField()
	channel = serializers.DictField()

class article_data():
	def __init__(self,article_id,url,caption,preview_image,preview_title,preview_text,channel_id,shared_from_article_id,created_at,user,channel):
		self.article_id = article_id
		self.url = url
		self.caption = caption
		self.preview_image = preview_image
		self.preview_title = preview_title
		self.preview_text = preview_text
		self.channel_id = channel_id
		self.shared_from_article_id = shared_from_article_id
		self.created_at = created_at
		self.user = user
		self.channel = channel
