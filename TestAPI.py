import time
import requests
from TestCases.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from requests_oauthlib import OAuth1


class Test_testApp(BaseClass):
    def test_searchButton(self):
        self.homePage = HomePage(self.driver)
        self.searchButton("//input[@id='searchbox']").send_keys("nokia")
        time.sleep(15)

    def test_searchSubmit(self):
        self.homePage = HomePage(self.driver)
        self.searchSubmit("#searchsubmit").click()
        time.sleep(15)


    def test_nokia(self):
        self.homePage = HomePage(self.driver)
        self.nokia("//a[text()='Nokia N800']").click()
        time.sleep(15)


    def test_save(self):
        self.homePage = HomePage(self.driver)
        self.save("//input[@value='Save this computer']").click()
        time.sleep(15)


    def test_searchComputer(self):
        self.homePage = HomePage(self.driver)
        self.searchButton("//input[@id='searchbox']").send_keys("ASCI Blue Pacific")
        time.sleep(5)
        self.searchSubmit("#searchsubmit").click()
        time.sleep(10)

    def test_auth(self) :
        url = "https://computer-database.gatling.io/computers"
        auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                      'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

        requests.get(url, auth=auth)
        print(auth.force_include_body)
        print(auth.client_class)


    def test_api_getAll(self):
        headers = {"Content-Type" : "application/json"}
        response_getAll = requests.get(url="https://computer-database.gatling.io/computers", headers=headers)
        if response_getAll.status_code == 404 :
            print(response_getAll.json())
        else:
            print('Status: {0}'.format(response_getAll.status_code))

        return headers


    def test_api_get(self) :
        resp = requests.get("https://computer-database.gatling.io/computers/513")
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)


