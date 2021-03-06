from django.db import connection
from functions import dictfetchall

def get_article_from_comment(comment_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM comment
            JOIN article
            ON article.article_id = comment.article_id
            WHERE comment.comment_id = %s
        """, [comment_id])
        return dictfetchall(cursor)

 
