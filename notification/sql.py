from django.db import connection

def get_notification_detail(self):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM notification;
        """)
        data = cursor.fetchall()
    return data
