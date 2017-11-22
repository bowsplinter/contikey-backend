from django.db import connection
from functions import dictfetchall

def userid_get_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user WHERE user_id = %s", [user_id])
        return dictfetchall(cursor)

def userid_get_channels(user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM channel WHERE user_id = %s", [user_id])
        return dictfetchall(cursor)

def facebookid_get_user(facebook_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user WHERE facebook_id = %s", [facebook_id])
        return dictfetchall(cursor)

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

def insert_user(data):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO user (facebook_id, name, email, photo) 
            VALUES (%s, %s, %s, %s)""",
            [data.get('facebook_id'), data.get('name'), data.get('email'), data.get('photo')])
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()[0]
        return user_id