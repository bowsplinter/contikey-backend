from rest_framework.views import APIView
from rest_framework.response import Response

from .sql import *

class notification_detail(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response(get_notification_detail(self))