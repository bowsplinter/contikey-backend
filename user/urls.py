from django.conf.urls import url

from . import views

urlpatterns = [
    # /user/
    url(r'^$', views.profile, name='profile'),
    # /user/2
    url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    # /user/2/channels/
    url(r'^(?P<user_id>[0-9]+)/channels/$', views.channels, name='user_channels'),
]