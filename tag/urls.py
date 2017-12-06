from django.conf.urls import url
from tag import views

urlpatterns = [
    # GET tag/
    url(r'^$', views.tag_list.as_view(), name='tag-list'),
    # POST tag/follow/
    url(r'^follow/$', views.user_tags.as_view(), name='follow-tags'),
]
