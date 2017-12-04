from django.db import connection
from functions import dictfetchall

# get user stats - user, articles, channels, friends, followed
def get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM user
            WHERE user_id = %s;
        """, [user_id])
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

#  get article stats - article, likes, comments, no_of_views

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

# get channel stats - channel, articles, followers

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

#  get user history

def get_user_history(user_id):
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
                SELECT NULL as channel_id, article_id, comment_id,
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
            """, [user_id])
        if cursor.fetchall():
            return dictfetchall(cursor)
        else:
            return {'error': 'history is empty'}
