import time

import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://reqres.in/")
time.sleep(10)


def test_api_get():
    resp = requests.get("https://reqres.in/api/users?page=2")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 4:
            assert record['first_name'] == "Eve",\
                "Data not matched! Expected : Eve, but found : " + str(record['first_name'])
            assert record['last_name'] == "Holt",\
                "Data not matched! Expected : Holt, but found : " + str(record['last_name'])
            time.sleep(5)


def test_api_post():
    data = {'name': 'John',
            'job': 'QA'}
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    assert (resp.status_code == 201), "Status code is not 201. Rather found : "\
        + str(resp.status_code)
    assert data['name'] == "John", "User created with wrong name. \
        Expected : John, but found : " + str(data['name'])
    assert data['job'] == "QA", "User created with wrong job. \
        Expected : QA, but found : " + str(data['name'])
    time.sleep(5)