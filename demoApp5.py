# https://jsonplaceholder.typicode.com/posts/1/comments
import requests


def test_api_putName():
    response_put_name = requests.get(url="https://jsonplaceholder.typicode.com/users/1/todos")
    # Check the response status code
    if response_put_name.status_code == 400:
        # Print the response content
        print(response_put_name.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_put_name.status_code))
        print(response_put_name.text)


