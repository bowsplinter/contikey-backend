from django.conf.urls import url

from . import views

urlpatterns = [
	# /article/new
    url(r'^new/$', views.new, name='new_article'),
    # /article/<channel_id>/<article_id>/like
    url(r'^like/$', views.like, name='like_article'),
    # /article/<channel_id>/<article_id>/comment
    url(r'^comment/$', views.comment, name='comment_article'),
]