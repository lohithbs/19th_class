from selenium import webdriver
import pytest
from data.data_file import *


@pytest.fixture(scope='class')
def test_launch_browser(request):
    global webdriver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()