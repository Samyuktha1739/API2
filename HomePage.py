from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def searchButton(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def searchSubmit(self, locator):
        return self.driver.find_element(By.ID, locator)

    def nokia(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def save(self, xpath):
        return self.driver.find_element(By.XPATH,xpath)

    def searchComputer(self, xpath):
        return self.driver.find_element(By.XPATH,xpath)

