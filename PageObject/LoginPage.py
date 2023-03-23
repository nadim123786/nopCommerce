from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
    
    def set_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)
    
    def set_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def click_logout(self):
        self.driver.find_element(By.XPATH, "//a[@href='/logout']").click()
    
