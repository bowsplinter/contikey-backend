from django.conf.urls import url
from tag import views

urlpatterns = [
    url(r'^$', views.tag_list.as_view(), name='tag-list'),
]