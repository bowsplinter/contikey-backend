### SQL helper functions for channels and articles ###

from django.db import connection
from functions import dictfetchall, dictfetchone

def channellist_get_articles(channelList):
    with connection.cursor() as cursor:
        for channel in channelList:
            cursor.execute("""
                SELECT * FROM article WHERE channel_id = %s
                LIMIT 4
                """,
                [channel['channel_id']])
            channel['articles'] = dictfetchall(cursor)
    return channelList

def channellist_get_user(channelList):
    with connection.cursor() as cursor:
        for channel in channelList:
            cursor.execute("""
                SELECT * FROM user WHERE user_id = %s
                """,
                [channel['user_id']])
            channel['user'] = dictfetchone(cursor)
    return channelList

def articlelist_get_channel(articleList):
    with connection.cursor() as cursor:
        for article in articleList:
            if not article['channel_id']:
                article['channel'] = None
            else:
                cursor.execute("SELECT * FROM channel WHERE channel_id = %s",
                    [article['channel_id']])
                article['channel'] = dictfetchone(cursor)
    return articleList

def articlelist_get_user(articleList):
    # use this with the result of articlelist_get_channel
    with connection.cursor() as cursor:
        for article in articleList:
            if not article['channel']['channel_id']:
                article['user'] = None
            else:
                cursor.execute("SELECT * FROM user WHERE user_id = %s",
                    [article['channel_id']])
                article['user'] = dictfetchone(cursor)
    return articleList