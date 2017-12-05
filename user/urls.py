from django.conf.urls import url

from . import views

urlpatterns = [
  # POST /user/login
  url(r'^login/$', views.login, name='login'),
  # POST /user/logout
  url(r'^logout/$', views.logout, name='logout'),

  # GET /user/
  url(r'^$', views.user_detail, name='profile'),
  # GET /user/2
  url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='profile'),

  # GET /user/channels/
  url(r'^channels/$', views.user_channels, name='user_channels'),
  # GET /user/2/channels/
  url(r'^(?P<user_id>[0-9]+)/channels/$', views.user_channels, name='user_channels'),

  # GET /user/articles/
  url(r'^articles/$', views.user_articles, name='user_articles'),
  # GET /user/2/articles/
  url(r'^(?P<user_id>[0-9]+)/articles/$', views.user_articles, name='user_articles'),

  # GET /user/friends/
  url(r'^friends/$', views.user_friends, name='user_friends'),
  # GET /user/2/friends/
  url(r'^(?P<user_id>[0-9]+)/friends/$', views.user_friends, name='user_friends'),

  # GET /user/following/
  url(r'^following/$', views.user_following, name='user_following'),
  # GET /user/2/following/
  url(r'^(?P<user_id>[0-9]+)/following/$', views.user_following, name='user_following'),

  # POST /user/follow_tag/
  url(r'^follow_tag/$', views.follow_tag, name='user_follow_tag'),

  # POST /user/2/follow_tag/
  url(r'^(?P<user_id>[0-9]+)/follow_tag/$', views.follow_tag, name='user_follow_tag'),

  # TODO:
  # POST /user/update - to update bio
]
