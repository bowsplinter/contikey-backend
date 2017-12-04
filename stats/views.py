from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall
from .sql import *
from comment.sql import get_article_from_comment

entity_ids = ['channel_id', 'article_id', 'comment_id', 'friend_id',
    'followed_channel_id', 'liked_article_id']
functionList =  {
    'channel': get_channel,
    'article': get_article,
    'comment': get_article_from_comment,
    'friend': get_user,
    'followed_channel': get_channel,
    'liked_article': get_article
}

@api_view(['GET'])
def get_user_stats(request, user_id):
    """
    - gets articles of user
    - gets channels of user
    - gets friends of user
    - gets followed channels of user
    """
    user = get_user(user_id)
    if user:
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
    else:
        return Response({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)

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
    history = []
    user_id = request.session['user_id']
    if user_id:
        user = get_user(user_id)[0]
        history_table = get_history_table(user_id)
        for entry in history_table:
            for entity_id in entity_ids:
                if entry[entity_id]:
                    name = entity_id.replace('_id', '')
                    sql_function = functionList[name]
                    data = {
                        name: sql_function(entry[entity_id])[0]
                    }
                    if name == 'comment':
                        data[name]['created_at'] = entry['created_at']
                    elif name == 'channel':
                        data[name]['user'] = user
                    elif name == 'followed_channel':
                        data[name]['user'] = get_user(data[name]['user_id'])
                    history.append(data)

        result = {
            'history': history,
            'user': user,
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'unable to get user_id'}, status=status.HTTP_400_BAD_REQUEST)
