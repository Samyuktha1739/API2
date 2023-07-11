import requests
from requests_oauthlib import OAuth1

url = 'https://gorest.co.in'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)
# <Response [200]>
print(auth.client)
print(auth.client_class)