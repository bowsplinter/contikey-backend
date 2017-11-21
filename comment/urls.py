from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from comment import views

urlpatterns = [
    url(r'^articles/(?P<article_id>[0-9]+)/comments$', views.article_comments),
    url(r'^comments/(?P<comment_id>[0-9]+)$', views.delete_comment)
]
