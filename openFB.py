from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
import env

class TestHomePage(unittest.TestCase):
     def test_enter_data(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        USER = os.getenv('API_USER')
        PASSWORD = os.environ.get('API_PASSWORD')
        user_email = driver.find_element_by_name("enter your email")
        user_email.send_keys(USER)
        user_passwd = driver.find_element_by_name("enter your passowrd")
        user_passwd.send_keys(PASSWORD)
        login = driver.find_element_by_id("u_0_b")
        login.click()
        assert 'No results' not in driver.page_source
        driver.close()

if __name__ == '__main__':
    unittest.main()
