import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/get/json"

headers = CaseInsensitiveDict()
headers["Cookie"] = "name=value; name2=value2"

response = requests.get(url, headers=headers)
# print(response)
# print(response.text)
print(response.status_code)