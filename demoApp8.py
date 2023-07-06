import requests

from demoApp7 import login_return_cookie


# This function will use server returned cookie for later url request.
def get_data():

    # First invoke login_return_cookie() method to login to the website and get server returned cookies value.
    cookie = login_return_cookie()

    # Request below url to vote, the vote action need login cookies.
    vote_url = 'http://www.test-abc.com/vote'
    # Pass server returned cookies to the vote_url request.
    response = requests.get(url=vote_url, cookies=cookie)

    print(response.text)
