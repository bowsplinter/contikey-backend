from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .sql import *

class notification_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try: # get user's user_id from session key
            user_id = request.session['user_id']
        except:
            return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(get_notification_list(user_id), status=status.HTTP_200_OK)