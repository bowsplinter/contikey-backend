from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^user/$', views.search_by_user.as_view(), name='search_by_user'),
    url(r'^channel/$', views.search_by_channel.as_view(), name='search_by_channel'),
    url(r'^article/$', views.search_by_article.as_view(), name='search_by_article'),
]
