from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import sql

@api_view(['GET'])
def search_by_user(request):
    """
    search by username: gets user + user's channels, articles, friends
    """
    username = request.GET.get('search_term', '')
    users = sql.get_users_by_username(username)
    return Response({'data': users}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_channel(request):
    """
    search by channel title: gets channel + channel's articles
    """
    title = request.GET.get('search_term', '')
    channels = sql.get_channels_by_title(title)
    return Response({'data': channels}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_by_article(request):
    """
    search by article title
    """
    title = request.GET.get('search_term', '')
    articles = sql.get_articles_by_title(title)
    return Response({'data': articles}, status=status.HTTP_200_OK)
