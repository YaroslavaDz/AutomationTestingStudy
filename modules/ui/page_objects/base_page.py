from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r'c:\\Users\\HP\\documents\\project1\\AutomationTestingStudy'
    DRIVER_NAME = 'chromdriver.exe'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))

    def close(self):
        self.driver.close()