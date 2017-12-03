from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^users/$', views.search_by_user, name='search_by_user'),
    url(r'^channels/$', views.search_by_channel, name='search_by_channel'),
    url(r'^articles/$', views.search_by_article, name='search_by_article'),
]
