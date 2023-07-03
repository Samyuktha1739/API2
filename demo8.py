from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://demoqa.com/")
cookies = driver.get_cookie()
print(len(cookies))
print(cookies)

cookie = {'name': 'Mycookie', 'values': '1234567890'}
driver.add_cookie(cookie)

driver.get("https://demoqa.com/")
cookies = driver.get_cookie()
print(len(cookies))
print(cookies)