from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import sql

# Create your views here.
@api_view(['GET','DELETE'])
def channel(request, channel_id):
	if request.method == 'GET':
		data, statusr = sql.get_channel(channel_id)
		return Response({'channel': data},status=statusr)

	elif request.method == 'DELETE':
		try:
			user_id = request.session['user_id']
		except:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

		data,statusr = sql.delete_channel(user_id,channel_id)
		return Response(data, status=statusr)

@api_view(['POST'])
def new(request):
	if request.method == 'POST':
		try:
			user_id = request.session['user_id']
			title = request.POST.get('title')
			description = request.POST.get('description')
		except KeyError as e:
			return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'error':'missing or invalid POST body'}, status=status.HTTP_400_BAD_REQUEST)		
		data, statusr = sql.create_channel(user_id,title,description)
		return Response(data, statusr)

@api_view(['POST','DELETE'])
def follow(request, channel_id):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'POST':
		data, statusr = sql.get_follow(user_id,channel_id)
		return Response(data, statusr)
	elif request.method == 'DELETE':
		data, statusr = sql.delete_follow(user_id,channel_id)
		return Response(data, statusr)

@api_view(['GET'])
def explore(request):
	try:
		user_id = request.session['user_id']
	except:
		return Response({'error':'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		limit = 10;
		data = sql.get_user_explore(user_id,limit)

	return Response({'channels': data},status=status.HTTP_200_OK)