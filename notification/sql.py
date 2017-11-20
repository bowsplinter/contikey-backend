from django.db import connection

def get_notification_detail(self):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM notification;
        """)
        data = cursor.fetchall()
    return data

def add_notification(self, data):
    text = data['text']
    url = data['url']
    user_id = data['user_id']

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO notification (text, url, user_id)
            VALUES (%s, %s, %s)
            """, [text, url, user_id])
    return 0
