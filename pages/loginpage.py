from data.data_file import *
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.UN="username"
        self.PWD="pwd"
        self.login_btn="//*[text()='Login ']"

    def enter_UN(self):
        self.driver.find_element_by_name(self.UN).send_keys(UN)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.PWD).send_keys(PWD)

    def enter_login(self):
        self.driver.find_element_by_xpath(self.login_btn).click()

