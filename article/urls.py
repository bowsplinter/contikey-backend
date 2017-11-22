from django.conf.urls import url

from . import views

urlpatterns = [
	#TODO:
	# GET DELETE /article/<article_id>/
	# > get comments from article
	# > delete article from here also
	# > get X most recent articles from followed channels
	url(r'^(?P<article_id>[0-9]+)/$', views.view, name='article'),
	# POST /article/new
    url(r'^new/$', views.new, name='new_article'),
    # POST /article/like
    url(r'^(?P<article_id>[0-9]+)/like/$', views.like, name='like_article'),
    # POST /article/comment
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment_article'),
    # GET /article/feed ?
    url(r'^feed/$', views.feed, name='feed')
]