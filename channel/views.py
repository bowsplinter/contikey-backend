from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import sql


#Should there be a lighter version of get?
class channel_helper(APIView):
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
		return Response({'channel': data},status=statusr)

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
			title = request.POST.get('title')
			description = request.POST.get('description')
			tags = request.POST.get('tags').split(',')
		except KeyError as e:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)		
		
		data, statusr = sql.create_channel(user_id,title,description,tags)
		#To autofollow own channel
		data, statusr = sql.new_follow(user_id,data)

		return Response(data, statusr)

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


class channel_explorer(APIView):
	"""
		get:
		This gets the user_id from the session,
		and pulls out relevant channels based on the users tag selection that he has NOT followed

		#TODO: Follow proper pagination from REST framework
	"""
	def get(self, request):
		limit = 10;

		try:
			user_id = request.session['user_id']
			data = sql.get_user_explore(user_id,limit)
			return Response({'channels': data},status=status.HTTP_200_OK)
		except:
			data = sql.get_nologin_explore(limit)
			return Response({'channels': data},status=status.HTTP_200_OK)

