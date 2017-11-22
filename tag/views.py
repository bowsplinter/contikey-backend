from rest_framework.views import APIView
from rest_framework.response import Response

from .sql import *

class tag_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response(get_tag_list(self))
