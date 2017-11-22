from django.conf.urls import url
from notification import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.notification_detail.as_view(), name='notification-list'),
]