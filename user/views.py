from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser
import functionssql as fs
from . import facebook as fb
from . import sql

@api_view(['POST'])
@parser_classes((JSONParser,MultiPartParser))
def login(request):
    """
    Log user in with FB access token after FB login is completed

    Fields: *accessToken: string
    Returns: user info, user's channels, new_user flag (True if user hasn't followed any tags)
    """
    accessToken = request.data.get('accessToken')
    if accessToken == None:
        return Response({'error': 'accessToken required'}, status=status.HTTP_400_BAD_REQUEST)

    facebook_id = fb.inspectUserToken(accessToken)
    if not facebook_id:
        return Response({'error': 'invalid accessToken'}, status=status.HTTP_401_UNAUTHORIZED)

    # check if user exists, else fetch fb profile and create user
    selectUser = sql.facebookid_get_user(facebook_id)
    if selectUser:
        newUser = False
        user_id = selectUser[0]['user_id']
    else:
        newUser = True
        u = fb.getUserInfo(accessToken)
        u['facebook_id'] = facebook_id
        user_id = sql.insert_user(u)
        if u.get('friends'):
            sql.insert_user_friends(user_id, [friend['id'] for friend in u['friends']])
    user = sql.userid_get_user(user_id)
    user['channels'] = sql.userid_get_channels(user_id)
    followedTags = sql.userid_get_tagids(user_id)

    request.session['user_id'] = user['user_id'] # store user_id in session data
    return Response({'user': user, 'new_user': not bool(followedTags)})

@api_view(['POST'])
def logout(request):
    """
    Log user out and clear session
    """
    if request.session.session_key == None:
        return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)

    request.session.flush() # delete session from DB and remove user's session cookie
    return Response({'success': True})

# GET request functions for user_detail and user edges use this template
# usage: call with the appropriate sql function
def get_template(request, user_id, sqlfunc = None):
    if user_id == 'me':
        try: # get user's user_id from session key
            user_id = request.session['user_id']
        except:
            return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)

    user = sql.userid_get_user(user_id)
    if not user:
        return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

    res = {'user': user}
    if sqlfunc:
        res['data'] = sqlfunc(user_id)
    return Response(res)

@api_view(['GET', 'DELETE'])
def user_detail(request, user_id = 'me'):
    """
    GET:
    Return user info for user_id (if specified) or the current user (default)

    DELETE:
    Delete user and clear session. Not authorized if user_id is specified
    """
    if request.method == 'GET':
        return get_template(request, user_id)
    elif request.method == 'DELETE':
        if user_id != 'me':
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_id = request.session['user_id']
        except:
            return Response({'error': 'no existing session or session expired'}, status=status.HTTP_400_BAD_REQUEST)
        success = sql.delete_user(user_id)
        if success:
            request.session.flush()
        return Response({'success': bool(success)})

@api_view(['GET'])
def user_channels(request, user_id = 'me'):
    """
    Return list of channels created by user_id (if specified) or the current user (default)
    """
    res = get_template(request, user_id, sql.userid_get_channels)
    #Success, now to get if user is subbed
    if res.status_code == 200:
        try: # get user's user_id from session key
            user_id = request.session['user_id']
            for channel in res.data['data']:
                fs.channel_get_subscribed(res.data['data'], user_id)
        except:
            for channel in res.data['data']:
                channel['subscribed'] = False
    return res

@api_view(['GET'])
def user_articles(request, user_id = 'me'):
    """
    Return list of articles posted in channels by user_id (if specified) or the current user (default)
    """
    return get_template(request, user_id, sql.userid_get_articles)

@api_view(['GET'])
def user_friends(request, user_id = 'me'):
    """
    Return list of friends of user_id (if specified) or the current user (default)
    """
    return get_template(request, user_id, sql.userid_get_friends)

@api_view(['GET'])
def user_following(request, user_id = 'me'):
    """
    Return list of channels followed by user_id (if specified) or the current user (default)
    """
    res = get_template(request, user_id, sql.userid_get_following)
    #Success, now to get if user is subbed
    if res.status_code == 200:
        try: # get user's user_id from session key
            user_id = request.session['user_id']
            for channel in res.data['data']:
                fs.channel_get_subscribed(res.data['data'], user_id)
        except:
            for channel in res.data['data']:
                channel['subscribed'] = False
    return res