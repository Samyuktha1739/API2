import requests

response_getId = requests.get('https://reqres.in/api/users/8')
# Check the response status code
if response_getId.status_code == 200:
    # Print the response content
    print(response_getId.json())
else:
    # Handle the error
    print('Error: {0}'.format(response_getId.status_code))
    print(response_getId.text)