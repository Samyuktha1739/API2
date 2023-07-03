import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)

getData_response = requests.get("https://gorest.co.in/public/v2/users")
print(getData_response)
print(getData_response.text)\

getId_response = requests.get("https://gorest.co.in/public/v2/users/1945")
print(getId_response)
print(getId_response.text)

putData_response = requests.patch("https://gorest.co.in/public/v2/users/1945")
print(putData_response)
print(putData_response.text)

deleteData_response = requests.delete("https://gorest.co.in/public/v2/users/1945")
print(deleteData_response)
print(deleteData_response.text)


postData1_response = requests.post("https://gorest.co.in/public/v2/users/1945/posts")
print(postData1_response)
print(postData1_response.text)