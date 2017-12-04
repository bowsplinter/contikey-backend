from django.conf.urls import url
from notification import views

urlpatterns = [
    url(r'^$', views.notification_list.as_view(), name='notification-list'),
    url(r'^(?P<notification_id>[0-9]+)/$', views.notification_detail.as_view(), name='notifcation-detail')
]