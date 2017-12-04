from django.http import JsonResponse
from django.db import connection
from django.core.paginator import Paginator
from rest_framework import status,serializers, pagination
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.utils.urls import replace_query_param
from . import sql

class channel_helper(APIView):
	parser_classes = (JSONParser,MultiPartParser)
	"""
		get:
		Given a channel_id from the url,
		this returns the Channel info, tags associated with the Channel and the distinct number of follows.

		delete:
		Given a channel_id from the url,
		this attempts to get the user_id from the session and delete the channel_id if it belongs to the user
		
		post:
		Given a user_id, title and description,
		this attempts to create a new channel under the given user
	"""
	def get(self,request, channel_id):
		data, statusr = sql.get_channel(channel_id)
		data['tags'] = sql.get_channel_tags(channel_id)[0]
		data['subscribers'] = sql.get_channel_follower_count(channel_id)[0]
		data['user'] = sql.get_channel_user(channel_id)[0]
		data['articles'] = sql.get_channel_articles(channel_id)[0]
		return Response(data,status=statusr)

	def delete(self,request,channel_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

		data,statusr = sql.delete_channel(user_id,channel_id)
		return Response(data, status=statusr)

	def post(self,request):
		try:
			user_id = request.session['user_id']
			title = request.data.get('title')
			description = request.data.get('description')
			tags = request.data.get('tags').split(',')
		except KeyError as e:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'error':'missing or invalid POST body','errorType':str(type(e)), 'errorArgs':e.args}, status=status.HTTP_400_BAD_REQUEST)		
		
		data, statusr = sql.create_channel(user_id,title,description,tags)
		#To autofollow own channel
		data, statusr = sql.new_follow(user_id,data)

		return Response(data, statusr)

#Best name
class channel_articler(APIView):
	"""
		get:
		Given a channel_id from the url,
		this attempts to get the articles associated with the channel and return them
	"""
	def get(self,request,channel_id):
		data, statusr = sql.get_channel_articles(channel_id)
		return Response(data,status=statusr)

class channel_follower(APIView):
	"""
		post:
		Given a channel_id from the url,
		this attempts to get the user_id from the session and add the user to follow the given channel

		delete:
		Given a channel_id from the url,
		this attempts to get the user_id from the session and remove the user from following the given channel
	"""
	def post(self,request,channel_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		data, statusr = sql.new_follow(user_id,channel_id)
		return Response(data, statusr)

	def delete(self,request,channel_id):
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		data, statusr = sql.delete_follow(user_id,channel_id)
		return Response(data, statusr)

class channel_recommender(APIView):
	"""
		get:
		This gets the user_id from the session,
		and pulls out relevant channels based on the users tag selection that he has NOT followed
	"""
	def get(self, request):
		try:
			user_id = request.session['user_id']
			queryset = sql.get_user_recommend(user_id)
		except:
			queryset = sql.get_nologin_recommend()
		paginator = channel_paginator()
		result_page = paginator.paginate_queryset(queryset,request)
		serializer = recommend_serializer(result_page, many=True)
		return Response({'channel':serializer.data},status=status.HTTP_200_OK)

class channel_paginator(pagination.PageNumberPagination):
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

class recommend_serializer(serializers.Serializer):
	channel_id = serializers.IntegerField()
	user_id = serializers.IntegerField()
	#These two should switch to 128 and 512 to be more efficient, Padded anyway.
	title = serializers.CharField(max_length=100)
	description = serializers.CharField(max_length=500)
	subscribers = serializers.IntegerField()
	user = serializers.DictField()

class recommend_data():
	def __init__(self,channel_id,user_id,title,description,subscribers,user):
		self.channel_id = channel_id
		self.user_id = user_id
		self.title = title
		self.description = description
		self.subscribers = subscribers
		self.user = user