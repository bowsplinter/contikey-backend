from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall

# """
# * Views all comments for an article
# * Post a comment in an article
# """
# @api_view(['GET', 'POST')
# def article_comments(request, article_id):
#     if request.method == 'GET':
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT *
#                 FROM comment
#                 WHERE article_id = %s;
#             """, article_id)
#             result = dictfetchall(cursor)
#         return Response(result ,status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         comment_text = data['comment_text']
#         user_id = request.session['user_id']
#         if user_id:
#             with connection.cursor() as cursor:
#                 cursor.execute("""
#                     INSERT INTO comment(comment_text, user_id, article_id, created_at)
#                     VALUES (%s, %s, %s, %s, NOW())
#                 """, [comment_text, user_id, article_id])
#                 result = dictfetchall(cursor)
#             return Response(result ,status=status.HTTP_201_CREATED)
#     `   else:
#             return Response(result, status=status.HTTP_401_UNAUTHORIZED)

"""
* Delete the user's own comment in an article
"""
@api_view(['DELETE'])
def delete_comment(request, comment_id):
    user_id = request.session['user_id']
    if user_id:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM comment
                WHERE user_id = %s
                AND comment_id = %s
            """, [user_id, comment_id])
            result = dictfetchall(cursor)
        return Response(result ,status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
