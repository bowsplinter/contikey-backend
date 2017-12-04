from django.conf.urls import url
from . import views

urlpatterns = [
	#GET/DELETE /channel/<channel_id>/
	url(r'^(?P<channel_id>[0-9]+)/$', views.channel_helper.as_view(), name='channels'),
	#POST /channel/<channel_id>/follow/
	url(r'^(?P<channel_id>[0-9]+)/follow/$', views.channel_follower.as_view(), name='follow_channel'),
	#GET /channel/<channel_id>/articles/
	url(r'^(?P<channel_id>[0-9]+)/articles/$', views.channel_articler.as_view()),
	#POST /channel/new/
	url(r'^new/$', views.channel_helper.as_view(), name='new_channel'),
	#GET /channel/recommended/
	url(r'^recommended/$', views.channel_recommender.as_view(), name='recommended'),	
]	