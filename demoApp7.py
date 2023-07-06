# Import python requets module.
import requests


def login_return_cookie():
    # The website login url.
    login_url = 'http://www.test-abc.com/login'

    # Custom request headers.
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }

    # The login form submit data.
    login_data = {
        "username": "jerry",
        "password": "888888"
    }

    try:
        # Send a post request to login_url with login_data.
        response = requests.post(url=login_url, headers=headers, data=login_data)

        # Get server response cookies.
        cookies = response.cookies

        # Convert cookies to a dictionary object.
        cookie = requests.utils.dict_from_cookiejar(cookies)

        # Return the dictionary object.
        return cookie

    except Exception as err:
        # When there are exceptions, print error message.
        print('Retrieve cookie fail：\n{0}'.format(err))