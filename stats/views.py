from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall

"""
GET stats/user/<user_id> get_user_stats
- gets articles of user
- gets channels of user
- gets friends of user
- gets followed channels of user
"""
@api_view(['GET'])
def get_user_stats(request, user_id):
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

def get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def get_user_articles(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM article
            WHERE channel_id in
                (SELECT channel_id
                FROM channel
                WHERE user_id= %s);
        """, user_id)
        result = dictfetchall(cursor)
    return result

def get_user_channels(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM channel
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def get_user_friends(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user_friends
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def get_user_followed_channels(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user_follows_channel
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result


"""
stats/articles/<article_id>
- gets comments from article
- gets likes of article
- gets no of views
- gets article attributes
"""
@api_view(['GET'])
def get_article_stats(request, article_id):
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
        result = cursor.fetchone()
    return result[0]

def get_article_comments(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
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
        result = cursor.fetchone()
    return result[0]


"""
stats/channels/<channel_id>
- gets no of articles
- gets no of followers
- gets channel attributes
"""
@api_view(['GET'])
def get_channel_stats(request, channel_id):
    channel = get_channel(channel_id)
    result = {
        'channel': channel,
        'data': {
            'articles': get_channel_articles(channel_id),
            'followers': get_channel_followers(channel_id)
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

def get_channel_articles(channel_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM  article
            WHERE channel_id = %s;
        """, channel_id)
        result = dictfetchall(cursor)
    return result

def get_channel_followers(channel_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user_follows_channel
            WHERE channel_id = %s;
        """, channel_id)
        result = dictfetchall(cursor)
    return result


"""
GET /stats/history
- gets all user actions
    - created channels
    - liked articles
    - posted articles
    - posted comments
    - made a friend
    - followed a channel
    - liked an article
"""
@api_view(['GET'])
def get_history(request):
    user_id = request.session['user_id']
    user = get_user(user_id)

    with connection.cursor() as cursor:
        cursor.execute("""
            SET @user_id = %s;
            SELECT * FROM (
                SELECT channel_id, NULL as article_id, NULL as comment_id,
                    NULL as friend_id, NULL as followed_channel_id,
                    NULL as liked_article_id, created_at
                    FROM channel WHERE user_id = @user_id
                UNION ALL
                SELECT channel_id, article_id, NULL as comment_id,
                    NULL as friend_id, NULL as followed_channel_id,
                    NULL as liked_article_id, created_at
                    FROM article WHERE channel_id in
                        (SELECT channel_id from channel where user_id = @user_id)
                UNION ALL
                SELECT NULL as channel_id, NULL as article_id, comment_id,
                    NULL as friend_id, NULL as followed_channel_id,
                    NULL as liked_article_id, created_at
                    FROM comment WHERE user_id = @user_id
                UNION ALL
                SELECT NULL as channel_id, NULL as article_id, NULL as comment_id,
                    friend_id, NULL as followed_channel_id,
                    NULL as liked_article_id, created_at
                    FROM user_friends WHERE user_id = @user_id
                UNION ALL
                SELECT NULL as channel_id, NULL as article_id, NULL as comment_id,
                    NULL as friend_id, channel_id as followed_channel_id,
                    NULL as liked_article_id, created_at
                    FROM user_follows_channel WHERE user_id = @user_id
                UNION ALL
                SELECT NULL as channel_id, NULL as article_id, NULL as comment_id,
                NULL as friend_id, NULL as followed_channel_id,
                article_id as liked_article_id, created_at
                    FROM user_likes_article WHERE user_id = @user_id
                ) T1
            ORDER BY created_at;
        """, user_id)
        result = dictfetchall(cursor)
    return result
