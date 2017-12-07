from django.db import connection
from functions import dictfetchall
import functionssql as fs

def get_users_by_username(username):
    username = "%" + username + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT * FROM user WHERE name LIKE %s
        ORDER BY created_at DESC; """
        , [username])
        users = dictfetchall(cursor)
    return users

def get_channels_by_title(title, user_id):
    title = "%" + title + "%"
    with connection.cursor() as cursor:
        cursor.execute("SET @search_term = %s", [title])
        cursor.execute("""
        SELECT * FROM channel WHERE title LIKE @search_term
        OR description LIKE @search_term
        ORDER BY created_at DESC;
        """)
        channels = dictfetchall(cursor)
        channels = fs.channellist_get_articles(channels)
        channels = fs.channellist_get_user(channels)
        channels = fs.channel_get_subscribed(channels, user_id)
    return channels

def get_articles_by_title(title):
    title = "%" + title + "%"
    with connection.cursor() as cursor:
        cursor.execute("SET @search_term = %s", [title])
        cursor.execute(
        """
        SELECT * FROM article
        WHERE preview_title LIKE @search_term
        OR url LIKE @search_term
        OR preview_text LIKE @search_term
        OR caption like @search_term
        ORDER BY created_at DESC;
        """)
        articles = dictfetchall(cursor)
        articles = fs.articlelist_get_channel(articles)
        articles = fs.articlelist_get_user(articles)
    return articles
