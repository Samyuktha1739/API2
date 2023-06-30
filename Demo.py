import requests


getData_response = requests.get("https://jsonplaceholder.typicode.com/users")

print(getData_response)
print(getData_response.text)

postData_response = requests.post("https://jsonplaceholder.typicode.com/users")

print(postData_response.text)
print(postData_response)