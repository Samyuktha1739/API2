import requests


def test_api_getId():
    response_getId = requests.get('https://reqres.in/api/users/8')
    # Check the response status code
    if response_getId.status_code == 200:
        # Print the response content
        print(response_getId.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_getId.status_code))
        print(response_getId.text)


def test_api_post():
    data = {'name': 'John', 'job': 'QA'}
    response_post = requests.post(url="https://reqres.in/api/users", data=data)
    # Check the response status code
    if response_post.status_code == 200:
        # Print the response content
        print(response_post.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_post.status_code))
        print(response_post.text)
