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

    # def test_deleteComputer(self):
    #     self.homePage = HomePage(self.driver)
    #     self.deleteComputer("//a[@class='btn']").click()
    #     time.sleep(14)

    def test_addComputer(self):
        self.homePage = HomePage(self.driver)
        self.addComputer("//a[@id='add']").click()
        time.sleep(15)

    def test_newComputer(self):
        self.homePage = HomePage(self.driver)
        self.newComputer("//input[@id='name']").send_keys("Nokia 9 PureView")
        self.newComputer("//input[@value='Create this computer']").click()
        time.sleep(15)



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
        assert (resp.status_code != 400), "Status code is not 200. Rather found : " + str(resp.status_code)

    def test_api_createComputer(self) :
        headers = {"Computer Name": "Nokia 9 PureView", "Introduced": "2019-03-17",
                   "Discontinued": "2022-04-17", "Company": "Nokia"}
        response_createComputer = requests.get(url="https://computer-database.gatling.io/computers",
                                                   headers=headers)
        if response_createComputer.status_code == 404 :
            print(response_createComputer.json())
        else :
            print('Status: {0}'.format(response_createComputer.status_code))

        return headers

    def test_api_create(self) :
        headers = {"Content-Type" : "application/json", "Host": "<calculated when request is sent>"}
        response_create= requests.get(url="https://computer-database.gatling.io/computers", headers=headers)
        if response_create.status_code == 404 :
            print(response_create.json())
        else :
            print('Status: {0}'.format(response_create.status_code))

        return headers
