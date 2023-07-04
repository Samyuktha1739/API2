import requests

response = requests.get("https://google.com/")
cookies = requests.get_cookie()
print(len(cookies))
print(cookies)