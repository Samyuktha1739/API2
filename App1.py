import requests
from requests_oauthlib import OAuth1

url = 'https://magento.softwaretestingboard.com/'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)
# <Response [200]>
print(auth.force_include_body)
print(auth.client_class)