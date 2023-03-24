from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        service = Service("D:\\drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        service = Service("D:\\drivers\\msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.headless = True
        preferences = {"download.default_directory":"C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\Downloads", "plugins.always_open_pdf_externally": True}
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", "preferences")
        driver = webdriver.Edge(service=service, options=options)
        return driver
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        service = Service("D:\\drivers\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
        options.set_preference("browser.download.manager.showWhenStart", False)
        options.set_preference("browser.download.folderlist", 2)
        options.set_preference("browser.download.dir", "C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\Downloads")
        driver = webdriver.Firefox(service=service, options=options)
        return driver
    

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
    
