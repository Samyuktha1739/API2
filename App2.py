import requests
from requests_oauthlib import OAuth1


def test_api_get():
    resp = requests.get("https://computer-database.gatling.io/computers/500")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)


def test_api_patch():
    headers = {"Content-Type": "application/json"}
    response_patch = requests.post(url="https://computer-database.gatling.io/computers/500", headers=headers)
    # Check the response status code
    if response_patch.status_code == 404:
        # Print the response content
        print(response_patch.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_patch.status_code))
        # print(response_patch.text)


def test_auth():
    url="https://computer-database.gatling.io/computers/500"
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

    requests.get(url, auth=auth)
    # <Response [200]>
    print(auth.force_include_body)
    print(auth.client_class)