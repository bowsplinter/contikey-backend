from django.db import connection
from functions import dictfetchall, dictfetchone

def userid_get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user WHERE user_id = %s", [user_id])
        return dictfetchone(cursor)

def userid_get_channels(user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM channel WHERE user_id = %s", [user_id])
        channellist = dictfetchall(cursor)
    return channellist_get_articles(channellist)

def userid_get_articles(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM article WHERE channel_id IN (
                SELECT channel_id FROM channel WHERE user_id = %s
            )""",
            [user_id])
        articles = dictfetchall(cursor)
    return articlelist_get_channel(articles)

def facebookid_get_user(facebook_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user WHERE facebook_id = %s", [facebook_id])
        return dictfetchone(cursor)

def userid_get_friends(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM user WHERE user_id IN (
                SELECT friend_id FROM user_friends WHERE user_id = %s
                UNION
                SELECT user_id FROM user_friends WHERE friend_id = %s
            )""",
            [user_id, user_id])
        return dictfetchall(cursor)

def userid_get_following(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM channel WHERE channel_id IN (
            SELECT channel_id FROM user_follows_channel WHERE user_id = %s
            )""",
            [user_id])
        channels = dictfetchall(cursor)
    return channellist_get_articles(channels)

def insert_user(data):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO user (facebook_id, name, email, photo)
            VALUES (%s, %s, %s, %s)""",
            [data.get('facebook_id'), data.get('name'), data.get('email'), data.get('photo')])
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()[0]
        return user_id

def insert_user_friends(user_id, friend_fbid_list):
    for friend_fbid in friend_fbid_list:
        friend_user = facebookid_get_user(friend_fbid)
        if not friend_user: # for development. this shouldn't be needed in production
            continue
        friend_userid = friend_user['user_id']
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO user_friends (user_id, friend_id)
                VALUES (%s, %s)""",
                [user_id, friend_userid])
    return True

def delete_user(user_id):
    with connection.cursor() as cursor:
        d = cursor.execute("DELETE FROM user WHERE user_id = %s", [user_id])
        return d

def user_follow_tag(user_id, tag_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO user_follows_tag (user_id, tag_id)
            VALUES (%s, %s)
        """,[user_id, tag_id])
    return True

# helper functions (not directly used in view)
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
