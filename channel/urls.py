from django.conf.urls import url
from . import views

urlpatterns = [
    #GET/DELETE /channel/<channel_id>/
    url(r'^(?P<channel_id>[0-9]+)/$', views.channel, name='channels'),
    #POST /channel/new/
    url(r'^new/$', views.new, name='new_channel'),
    #POST /channel/<channel_id>/follow/
    url(r'^(?P<channel_id>[0-9]+)/follow/$', views.follow, name='follow_channel'),
    #GET channel/explore/
    url(r'^explore/$', views.explore, name='explore')
]	