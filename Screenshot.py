from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)

#driver.save_screenshot("/Users/chandrashekarbasavaraj/Downloads/sample.png")
driver.get_screenshot_as_file("/Users/chandrashekarbasavaraj/Downloads/sample.jpg")
