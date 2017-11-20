import requests

endpoint = 'https://graph.facebook.com/v2.11/'
appAccessToken = '1151319251668955|-jBHg6LI_g_TmFGHTNEdqgrnMyY'
appID = '1151319251668955'

def inspectUserToken(userToken):
  tokens = {'input_token': userToken, 'access_token': appAccessToken}
  try:
    res = requests.get(endpoint+'debug_token', params=tokens)
    data = res.json()['data']
    if data['is_valid'] and data['app_id'] == appID:
      return data['user_id']
    else:
      return False
  except:
    return False

def getUserInfo(userToken):
  token = {'access_token': userToken}
  res = requests.get(endpoint+'me?fields=name,email,picture', params=token)
  data = res.json()
  name = data.get('name')
  email = data.get('email')
  photo = data.get('picture')
  if photo:
    photo = photo['data']['url']
  res1 = requests.get(endpoint+'me/friends', params=token)
  data = res1.json()
  friends = data.get('data')
  return { 'name': name, 'email': email, 'photo': photo, 'friends': friends }