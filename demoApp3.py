import requests


def test_api_get():
    response_get = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    if response_get .status_code == 200:
        print(response_get .json())
    else:
        print('Error: {0}'.format(response_get .status_code))
        print(response_get .text)


def test_api_getId():
    response_getId = requests.get('https://jsonplaceholder.typicode.com/posts/?id=3')
    if response_getId.status_code == 200:
        print(response_getId.json())
    else:
        print('Error: {0}'.format(response_getId.status_code))
        print(response_getId.text)



def test_api_post():
    data = {
        "userId": 1,
        "id": 25,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem "
                "doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    }
    response_post = requests.post(url="https://jsonplaceholder.typicode.com/posts/", data=data)
    # Check the response status code
    if response_post.status_code == 200:
        # Print the response content
        print(response_post.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_post.status_code))
        print(response_post.text)


def test_api_delete():
    data = {"id": "2"}
    response_post = requests.delete(url="https://jsonplaceholder.typicode.com/posts/?id=2", data=data)
    # Check the response status code
    if response_post.status_code == 200:
        # Print the response content
        print(response_post.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_post.status_code))
        print(response_post.text)


def test_api_put():
    data = {"userId": 1, "id": 10}
    response_put = requests.put(url="https://jsonplaceholder.typicode.com/posts/?id=2", data=data)
    # Check the response status code
    if response_put.status_code == 200:
        # Print the response content
        print(response_put.json())
    else:
        # Handle the error
        print('Error: {0}'.format(response_put.status_code))
        print(response_put.text)



