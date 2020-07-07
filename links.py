from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.implicitly_wait(5)

links = driver.find_elements_by_tag_name("a")
print(len(links))

for link in links:
    print(link.text)

#driver.find_element_by_link_text("Register").click()
driver.find_element_by_partial_link_text("REG").click()
