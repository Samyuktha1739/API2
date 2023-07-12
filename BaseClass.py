
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def searchButton(self, xpath):
        searchButton = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return searchButton

    def searchSubmit(self, locator):
        searchSubmit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        return searchSubmit

    def nokia(self, xpath):
        nokia = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return nokia

    def save(self, xpath):
        save = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return save

    def searchComputer(self, xpath):
        searchSubmit = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return searchSubmit

