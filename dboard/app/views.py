from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from dboard.app.serializers import UserSerializer
from rest_framework import generics

# endpoints are created in the views - http://www.django-rest-framework.org/tutorial/3-class-based-views/
#
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
