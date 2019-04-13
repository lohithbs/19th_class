class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_link_xpath="//*[@id='logoutLink']"

    def logout_page(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
