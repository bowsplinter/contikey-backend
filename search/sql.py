from django.db import connection
from functions import dictfetchall
import functionssql as fs

def get_users_by_username(username):
    username = "%" + username + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT * FROM user WHERE name LIKE %s; """
        , [username])
        users = dictfetchall(cursor)
    return users

def get_channels_by_title(title):
    title = "%" + title + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """SELECT * FROM channel WHERE title LIKE %s; """
        , [title])
        channels = dictfetchall(cursor)
        channels = fs.channellist_get_articles(channels)
        channels = fs.channellist_get_user(channels)
    return channels

def get_articles_by_title(title):
    title = "%" + title + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT * FROM article
        WHERE preview_title LIKE %s;
        """
        , [title])
        articles = dictfetchall(cursor)
        articles = fs.articlelist_get_channel(articles)
        articles = fs.articlelist_get_user(articles)
    return articles
