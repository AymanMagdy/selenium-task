from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
class TestHomePage(unittest.TestCase):
     def test_enter_data(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        self.assertIn('Python', driver.title)
        driver_element = driver.find_element_by_name("q")
        driver_element.send_keys('pycon')
        driver_element.send_keys(Keys.RETURN)
        assert 'No results' not in driver.page_source
        driver.close()


if __name__ == '__main__':
    unittest.main()
