from django.conf.urls import url
from . import views

urlpatterns = [
    #GET/DELETE /channel/<channel_id>/
    url(r'^(?P<channel_id>[0-9]+)/$', views.channel_helper.as_view(), name='channels'),
    #POST /channel/new/
    url(r'^new/$', views.channel_helper.as_view(), name='new_channel'),
    #POST /channel/<channel_id>/follow/
    url(r'^(?P<channel_id>[0-9]+)/follow/$', views.channel_follower.as_view(), name='follow_channel'),
    #GET channel/explore/
    url(r'^explore/$', views.channel_explorer.as_view(), name='explore')
]	