from functions import dictfetchall
from django.db import connection

def get_user_feed(user_id, offset, items_per_page):
	with connection.cursor() as cursor:
		cursor.execute('SELECT * FROM article WHERE channel_id IN(SELECT channel_id FROM user_follows_channel WHERE user_id = %s) ORDER BY created_at DESC LIMIT %s,%s', [user_id,offset,items_per_page])
	return dictfetchall(cursor)