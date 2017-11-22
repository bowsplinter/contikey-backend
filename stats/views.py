from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall

"""
GET stats/user/<user_id> get_user_stats
- gets number of articles per user
- gets number of channels per user
- gets number of friends per user
- gets number of following per user
"""
@api_view(['GET'])
def get_user_stats(user_id):
    user = get_user(user_id)

    result = {
    'user': user,
    'data': {
        'no_of_articles': articles_per_user(user_id),
        'no_of_channels': channels_per_user(user_id),
        'no_of_followers': followers_per_user(user_id),
        'no_of_following': following_per_user(user_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)

def get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def no_of_articles(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM article
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def no_of_channels(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM channel
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def no_of_friends(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM user_friends
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def no_of_following(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM user_follows_channel
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result


"""
stats/article/<article_id>
- gets no of comments
- gets no of likes
- gets no of views
- gets article attributes
"""
@api_view(['GET'])
def get_article_stats(article_id):
    article = get_article(article_id)
    result = {
        'article': article,
        'data': {
            'no_of_likes': no_of_likes(article_id),
            'no_of_comments': no_of_comments(article_id),
            'no_of_views': no_of_views(article_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)

def get_article(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM article
            WHERE article_id = %s;
        """, article_id)
        result = dictfetchall(cursor)
    return result

def no_of_likes(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM user_likes_article
            WHERE article_id = %s;
        """, article_id)
        result = dictfetchall(cursor)
    return result

def no_of_comments(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM comment
            WHERE article_id = %s;
        """, article_id)
        result = dictfetchall(cursor)
    return result

def no_of_views(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM view
            WHERE article_id = %s;
        """, article_id)
        result = dictfetchall(cursor)
    return result


"""
stats/channel/<channel_id>
- gets no of articles
- gets no of followers
- gets channel attributes
"""
@api_view(['GET'])
def get_channel_stats(channel_id):
    channel = get_channel(channel_id)
    result = {
        'channel': channel,
        'data': {
            'no_of_articles': no_of_articles(channel_id),
            'no_of_followers': no_of_comments(channel_id)
        }
    }
    return Response(result ,status=status.HTTP_200_OK)

def get_channel(channel_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM channel
            WHERE channel_id = %s;
        """, channel_id)
        result = dictfetchall(cursor)
    return result

def no_of_articles(channel_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM  article
            WHERE channel_id = %s;
        """, channel_id)
        result = dictfetchall(cursor)
    return result

def no_of_followers(channel_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM user_follows_channel
            WHERE channel_id = %s;
        """, channel_id)
        result = dictfetchall(cursor)
    return result


"""
GET /stats/history
- gets all user actions
    - viewed articles
    - liked articles
    - posted articles
    - posted comments
    - created channels
"""
@api_view(['GET'])
def get_history(request):
    user_id = request.session['user_id']
    user = get_user(user_id)

    #TODO: join the tables (view, user_likes_article, article, comment, channel)
    # and sort by created_at
    return 
