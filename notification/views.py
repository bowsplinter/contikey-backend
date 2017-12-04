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
        return Response(get_notification_list(0), status=status.HTTP_200_OK)

class notification_detail(APIView):
    """
    POST to set notification as read
    -----------
    pararms
    -----------
    is_read: 1 for True, 0 for false
    """
    def post(self, request, notification_id, format=None):
        is_read = request.POST['is_read']
        success = set_notification_read(notification_id, is_read)
        return Response({'success': bool(success)}, status=status.HTTP_200_OK)