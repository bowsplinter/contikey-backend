from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser

from user.sql import userid_get_user
from .sql import *

class tag_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response(get_tag_list(), status=status.HTTP_200_OK)

class user_tags(APIView):
    parser_classes = (JSONParser,MultiPartParser)
    """
    post: Follow tag by tag_ids (list) for the current user
    """
    def post(self, request):
        try: # get user's user_id from session key
            user_id = request.session['user_id']
        except:
            return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = userid_get_user(user_id)
        if not user:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        tag_ids = request.data.get('tag_ids')
        if not tag_ids:
            return Response({'error': 'tag_ids required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            success = user_follow_tag(user_id, tag_ids)
        except:
            success = False;
        return Response({'success': bool(success)})
