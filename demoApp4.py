import requests


def test_api_put():
    data = {'name': 'morpheus', 'job': 'zion resident'}
    response_put = requests.put(url="https://reqres.in/api/users/2", data=data)
    # Check the response status code
    if response_put.status_code == 200:
        # Print the response content
        print(response_put.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_put.status_code))
        print(response_put.text)


def test_api_putName():
    data = {'name': 'Samyuktha', 'job': 'zion resident'}
    response_put_name = requests.put(url="https://reqres.in/api/users/2", data=data)
    # Check the response status code
    if response_put_name.status_code == 200:
        # Print the response content
        print(response_put_name.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_put_name.status_code))
        print(response_put_name.text)