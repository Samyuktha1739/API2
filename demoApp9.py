import requests


def get_data():
    # Get server response cookie string.
    cookie_string = login_return_cookie_string()

    # Set the cookie string in http request headers.
    headers = {
        "cookie": cookie_string
    }

    # Send get request with above custom headers(contains the cookies).
    response = requests.get(url=get_data_url, headers=headers)

    print(response.text)