from django.conf.urls import url
from notification import views

urlpatterns = [
    url(r'^$', views.notification_list.as_view(), name='notification-list'),
]