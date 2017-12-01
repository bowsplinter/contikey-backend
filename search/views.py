from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import sql

@api_view(['GET'])
def search_by_user(request):
    """
    search by username
    """
    username = request.GET.get('search_term', '')
    users = sql.get_users_by_username(username)
    if not users:
        return Response({'error': 'no users found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'data': users}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_channel(request):
    """
    search by channel title
    """
    title = request.GET.get('search_term', '')
    channels = sql.get_channels_by_title(title)
    if not channels:
        return Response({'error': 'no channel found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'data': channels}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_article(request):
    """
    search by article title
    """
    title = request.GET.get('search_term', '')
    articles = sql.get_articles_by_title(title)
    if not articles:
        return Response({'error': 'no articles found by that name'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'data': articles}, status=status.HTTP_200_OK)
