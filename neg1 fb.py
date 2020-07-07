from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/drivers for selenium/chromedriver-1")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://facebook.com")
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
search_bar = driver.find_element_by_name("email")
search_bar.send_keys("megha.cv27@gmail.com")

search_bar = driver.find_element_by_name("pass")
search_bar.send_keys("decemberdecember27")
search_bar.submit()