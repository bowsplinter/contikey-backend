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

  # GET /user/friends/
  url(r'^friends/$', views.user_friends, name='user_friends'),
  # GET /user/2/friends/
  url(r'^(?P<user_id>[0-9]+)/friends/$', views.user_friends, name='user_friends'),

  # TODO:
  # POST /user/update - to update bio
  # GET /user/2/following
]