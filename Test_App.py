import time

from TestCases.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Test_testApp(BaseClass):

    def test_searchButton(self):
        self.homePage= HomePage(self.driver)
        self.searchButton("//label[@data-role='minisearch-label']").click()
        time.sleep(15)
