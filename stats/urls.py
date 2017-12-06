from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stats import views

urlpatterns = [
	#GET stats/user/
    url(r'^user/(?P<user_id>[0-9]+)$', views.get_user_stats),
    #GET stats/articles/<article_id>
    url(r'^articles/(?P<article_id>[0-9]+)$', views.get_article_stats),
    #GET stats/channels/<channel_id>
    url(r'^channels/(?P<channel_id>[0-9]+)$', views.get_channel_stats),
    #GET stats/history/
    url(r'^history$', views.get_history),
]
