import pytest
from selenium import webdriver
from data import Data

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    Data.browser_name = request.param
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()