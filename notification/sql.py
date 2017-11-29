from django.db import connection
from functions import dictfetchall

from user.sql import userid_get_user

def get_notification_list(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM notification
            WHERE user_id = %s;
        """, [user_id])
        data = dictfetchall(cursor)
        for notification in data:
            type_user_id = notification['type_user_id']
            notification['type_user'] = userid_get_user(type_user_id)
    return {"data": data}

def add_notification(data):
    text = data['text']
    url = data['url']
    user_id = data['user_id']

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO notification (text, url, user_id)
            VALUES (%s, %s, %s)
            """, [text, url, user_id])
    return 0

def delete_notification(id):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM notification
            WHERE notification_id = %s
        """, [id])
    return 0
