from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .sql import *

class notification_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, user_id, format=None):
        return Response(get_notification_list(user_id), status=status.HTTP_200_OK)