from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^user/$', views.search_by_user, name='search_by_user'),
    url(r'^channel/$', views.search_by_channel, name='search_by_channel'),
    url(r'^article/$', views.search_by_article, name='search_by_article'),
]
