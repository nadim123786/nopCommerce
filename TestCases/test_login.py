from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.LoginPage import Login
from Utilities.customLogger import Loggen
from Utilities.readProperties import ReadData


class Test_login_001:
    baseURL = ReadData.read_baseURL()
    email = ReadData.read_email()
    password = ReadData.read_password()
    
    logger = Loggen.loggen()
    
    def test_homepage(self, setup):
        self.logger.info("Test_login_001")
        self.logger.info("Started HomePage test Case")
        self.driver = setup
        self.logger.info("opening URL")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("LoginPage Test case passed")
            self.driver.close()
            assert True
            
        else:
            self.logger.info("LoginPage Test case Failed")
            self.driver.save_screenshot("C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\ScreenShots\\loginPage.png")
            assert False
    
    def test_login(self, setup):
        self.logger.info("Test_login_002")
        self.logger.info("Started Login Test Case")
        self.driver = setup
        self.logger.info("opening URL")
        self.driver.get(self.baseURL)
        self.logger.info("Creating Login Page Object")
        self.login_page = Login(self.driver)
        self.logger.info("Entering admin email")
        self.login_page.set_email(self.email)
        self.logger.info("Entering password")
        self.login_page.set_password(self.password)
        self.logger.info("Clicking Login Button")
        self.login_page.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("Test case passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.save_screenshot("C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\ScreenShots\\login.png")
            self.driver.close()
            assert False
            