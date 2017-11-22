from django.conf.urls import url

from . import views

urlpatterns = [
  # POST /user/login
  url(r'^login/$', views.login, name='login'),
  # POST /user/logout
  url(r'^logout/$', views.logout, name='logout'),
  # GET /user/
  url(r'^$', views.profile, name='profile'),
  # GET /user/2
  url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
  # GET /user/2/channels/
  url(r'^(?P<user_id>[0-9]+)/channels/$', views.channels, name='user_channels'),

  # TODO:
  # POST /user/update - to update bio
  # GET /user/2/friends
  # GET /user/2/following
  # GET /user/channels
]