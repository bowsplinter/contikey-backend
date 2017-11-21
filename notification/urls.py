from django.conf.urls import url
from notification import views

urlpatterns = [
    url(r'^$', views.notification_detail.as_view(), name='notification-list'),
]