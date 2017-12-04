from django.conf.urls import url
from . import views

urlpatterns = [
    # GET DELETE /article/<article_id>/
    # > get X most recent articles from followed channels -> to feed?
    url(r'^(?P<article_id>[0-9]+)/$', views.article_helper.as_view(), name='article'),
    # POST /article/new
    url(r'^new/$', views.article_helper.as_view(), name='new_article'),
    # POST /article/like
    url(r'^(?P<article_id>[0-9]+)/like/$', views.article_liker.as_view(), name='like_article'),
    # POST /article/comment
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.article_commenter.as_view(), name='comment_article'),
    # GET /article/feed
    url(r'^feed/$', views.article_feeder.as_view(), name='feed')
]