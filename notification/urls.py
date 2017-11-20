from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notification import views

urlpatterns = [
    url(r'^$', views.notification_detail.as_view(), name='notification-list'),
]