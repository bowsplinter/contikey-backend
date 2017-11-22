from django.db import connection
from functions import dictfetchall

def get_tag_list(self):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM tag;
        """)
        data = dictfetchall(cursor)
    return {"status": 200,"data": data}

def add_tag(self, data):
    label = data['label']
    image = data['image']

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO tag (label, image)
            VALUES (%s, %s)
            """, [label, image])
    return 0

def delete_tag(self, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM tag
            WHERE tag_id = %s
        """, [id])
    return 0