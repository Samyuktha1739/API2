import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def searchButton(self, xpath):
        searchButton = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_selected((By.XPATH, xpath)))
        return searchButton