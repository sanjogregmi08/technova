class HomePage:
    link_login_xpath = '/html/body/section[1]/nav/div/ul/li/a'

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()
