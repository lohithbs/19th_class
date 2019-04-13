import time

from selenium import webdriver
from data.data_file import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
import pytest

@pytest.mark.usefixtures("test_launch_browser")
class Testlogin:
    def test_login(self):
        driver=self.driver
        lp=LoginPage(driver)
        lp.enter_UN()
        lp.enter_pwd()
        lp.enter_login()

    def test_logout(self):
        driver=self.driver
        time.sleep(5)
        hp=HomePage(driver)
        hp.logout_page()


