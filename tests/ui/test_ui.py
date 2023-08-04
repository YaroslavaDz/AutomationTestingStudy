import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Creating an object to control the browser
    driver = webdriver.Chrome(
        service=Service(r'c:\\Users\\HP\\documents\\project1\\AutomationTestingStudy' + 'chromdriver.exe')
    )
    # Opening the https://github.com/login page
    driver.get('https://github.com/login')

    # Finding the field in which we will enter the incorrect username or email address
    login_elem = driver.find_element(By.ID, 'login_field')

    # Entering the incorrect username or email address
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')

    # Finding the field in which we will enter the incorrect password
    pass_elem = driver.find_element(By.ID, 'password')

    # Entering the incorrect password
    pass_elem.send_keys('wrong password')

    # Finding the 'Sign in' button
    btn_elem = driver.find_element(By.NAME, 'commit')

    # Clicking the 'Sign in' button
    btn_elem.click()

    # Checking that the name of the page is what we expect
    assert driver.title == 'Sign in to GitHub · GitHub'

    driver.close()
