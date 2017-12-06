from django.conf.urls import url
from search import views

urlpatterns = [
	#GET search/users/
    url(r'^users/$', views.search_by_user, name='search_by_user'),
    #GET search/channels/
    url(r'^channels/$', views.search_by_channel, name='search_by_channel'),
    #GET search/articles/
    url(r'^articles/$', views.search_by_article, name='search_by_article'),
]
