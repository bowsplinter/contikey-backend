from django.db import connection
from functions import dictfetchall

def get_users_by_username(username):
    with connection.cursor() as cursor:
        cursor.execute(
        """SELECT * FROM user WHERE name LIKE %s; """
        , [username])
    return dictfetchall(cursor)

def get_channels_by_title(title):
    with connection.cursor() as cursor:
        cursor.execute(
        """SELECT * FROM channel WHERE title LIKE %s; """
        , [title])
    return dictfetchall(cursor)

def get_articles_by_title(title):
    with connection.cursor() as cursor:
        cursor.execute(
        """SELECT * FROM article WHERE title LIKE %s; """
        , [title])
    return dictfetchall(cursor)
