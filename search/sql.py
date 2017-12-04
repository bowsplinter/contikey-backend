from django.db import connection
from functions import dictfetchall
from user.sql import userid_get_user, userid_get_channels, userid_get_articles, userid_get_friends
from channel.sql import get_channel_articles, get_channel

def get_users_by_username(username):
    username = "%" + username + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT * FROM user WHERE name LIKE %s; """
        , [username])
        users = dictfetchall(cursor)
        # additional user info not needed atm
        # for user in users:
        #     user_id = user['user_id']
        #     user['channels'] = userid_get_channels(user_id)
        #     user['articles'] = userid_get_articles(user_id)
        #     user['friends'] = userid_get_friends(user_id)
    return users

def get_channels_by_title(title):
    title = "%" + title + "%"
    with connection.cursor() as cursor:
        cursor.execute(
        """SELECT * FROM channel WHERE title LIKE %s; """
        , [title])
        channels = dictfetchall(cursor)
        for channel in channels:
            channel_id = channel['channel_id']
            channel['articles'] = get_channel_articles(channel_id)[0]
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
        for article in articles:
            channel_id = article['channel_id']
            article['channel'] = get_channel(channel_id)[0]
    return articles
