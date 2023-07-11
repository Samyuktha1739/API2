# Authentication in Requests with HTTPDigestAuth
import requests
from requests.auth import HTTPDigestAuth
auth = HTTPDigestAuth('user', 'pass')

print(requests.get('https://www.google.com/', auth=auth))

# Returns: <Response [200]>