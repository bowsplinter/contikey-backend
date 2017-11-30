from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall
from .sql import *

@api_view(['GET'])
def get_user_stats(request, user_id):
    """
    - gets articles of user
    - gets channels of user
    - gets friends of user
    - gets followed channels of user
    """
    user = get_user(user_id)

    result = {
    'user': user,
    'data': {
        'articles': get_user_articles(user_id),
        'channels': get_user_channels(user_id),
        'friends': get_user_friends(user_id),
        'followed': get_user_followed_channels(user_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_article_stats(request, article_id):
    """
    - gets comments from article
    - gets likes of article
    - gets no of views
    - gets article attributes
    """
    article = get_article(article_id)
    result = {
        'article': article,
        'data': {
            'likes': no_of_likes(article_id),
            'comments': get_article_comments(article_id),
            'views': no_of_views(article_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)


@api_view(['GET'])
def get_channel_stats(request, channel_id):
    """
    - gets no of articles
    - gets no of followers
    - gets channel attributes
    """
    channel = get_channel(channel_id)
    result = {
        'channel': channel,
        'data': {
            'articles': get_channel_articles(channel_id),
            'followers': get_channel_followers(channel_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_history(request):
    """
    - gets all user actions:
        - created channels
        - liked articles
        - posted articles
        - posted comments
        - made a friend
        - followed a channel
        - liked an article
    """
    user_id = request.session['user_id']
    user = get_user(user_id)
    history = get_history(user_id)

    result = {
        'user': user,
        'history': history
    }
    return Response(result ,status=status.HTTP_200_OK)
