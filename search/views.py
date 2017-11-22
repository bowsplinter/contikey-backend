from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import sql

"""
SEARCH
search_by_user: gets closest matches by usernames
search_by_channel: gets closest matches by channel title
search_by_article: gets 10 closest matches by article title
"""

@api_view(['GET'])
def search_by_user(request):
    username = request.data['search_term']
    users = sql.get_users_by_username(username)
    if not users:
        return Response({'error': 'no users found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'users': users}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_channel(request):
    title = request.data['search_term']
    channels = sql.get_channels_by_title(title)
    if not channels:
        return Response({'error': 'no channel found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'channels': channels}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_article(request):
    title = request.data['search_term']
    articles = sql.get_articles_by_title(title)
    if not articles:
        return Response({'error': 'no articles found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'articles': articles}, status=status.HTTP_200_OK)
