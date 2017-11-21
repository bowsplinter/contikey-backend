from django.conf.urls import url
from . import views

urlpatterns = [
    # /explore
    # /feed
    #GET /channel/ - defaults to view channel 1
    url(r'^$', views.channel, name='channels'),
    #GET /channel/<channel_id>/
    url(r'^(?P<channel_id>[0-9]+)/$', views.channel, name='channels'),
    #POST /channel/new
    url(r'^new/$', views.new, name='new_channel'),
    #POST /channel/follow
    url(r'^follow/$', views.follow, name='follow_channel'),
]	