from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)

search_bar = driver.find_element_by_name("q")

time.sleep(3)


actions = ActionChains(driver)
actions.context_click(search_bar).perform()