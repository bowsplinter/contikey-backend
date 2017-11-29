from django.db import connection
from functions import dictfetchall

def get_tag_list():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM tag;
        """)
        data = dictfetchall(cursor)
    return {"data": data}

def add_tag(data):
    tag_id = data['tag_id']
    label = data['label']
    image = data['image']

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO tag (tag_id, label, image)
            VALUES (%s, %s, %s)
            """, [tag_id, label, image])
    return 0

def delete_tag(id):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM tag
            WHERE tag_id = %s
        """, [id])
    return 0

def delete_all_tags():
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM tag
        """)
    return 0