from django.conf.urls import url

from . import views

urlpatterns = [
	# /article/new
    url(r'^new/$', views.new, name='new_article'),
    # /article/like
    url(r'^like/$', views.like, name='like_article'),
    # /article/comment
    url(r'^comment/$', views.comment, name='comment_article'),
]