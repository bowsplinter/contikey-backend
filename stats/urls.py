from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stats import views

urlpatterns = [
    url(r'^user/(?P<user_id>[0-9]+)$', views.get_user_stats),
    url(r'^articles/(?P<article_id>[0-9]+)$', views.get_article_stats),
    url(r'^channels/(?P<channel_id>[0-9]+)$', views.get_channel_stats),
    url(r'^history$', views.get_history),
]
