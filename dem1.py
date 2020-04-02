from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
driver_element = driver.find_element_by_name("q")
driver_element.clear()
driver_element.send_keys("pycon")
driver_element.send_keys(Keys.RETURN)
assert "No results." not in driver.page_source
driver.close()
