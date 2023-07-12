import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': '/path/to/dir'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://computer-database.gatling.io/computers")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
