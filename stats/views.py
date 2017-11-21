from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from functions import dictfetchall

"""
GET_PROFILE
likes_per_article: gets number of likes of an article for any user
articles_per_user: gets number of articles of a logged in user

clicks_per_article: gets number of clicks of an article of a logged in user
followers_per_user: gets followers of a logged in user
following_per_user: gets following of a logged in user
channels_per_user: gets number of created channels of a logged in user
popular_articles: gets top 10 most popular articles of a logged in user

GET_RECOMMENDATIONS
recommended_channels: gets top channel from each liked tag
delete_recommendation: (? recommendation should be an entity?)

SEARCH
search_by_user: gets closest matches by usernames
search_by_tag: gets 10 most popular channels in that tag
search_by_article: gets 10 closest matches by article title
"""
@api_view(['GET'])
def get_profile(request):
    user_id = request.session['user_id']
    articles = articles_per_user(user_id)
    likes = likes_per_article(request.data['article_id'])
    result = {'user_id': user_id, 'articles': articles, 'likes': likes}
    return Response(result ,status=status.HTTP_200_OK)

def articles_per_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM article
            WHERE user_id = %s;
        """, user_id)
        result = dictfetchall(cursor)
    return result

def likes_per_article(article_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT count(*)
            FROM user_likes_article
            WHERE article_id = %s;
        """, article_id)
        result = dictfetchall(cursor)
    return result
