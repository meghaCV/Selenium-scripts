from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")

driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
time.sleep(3)

driver.switch_to_frame(0)
male = driver.find_element_by_xpath("/html/body/form/div[2]/div[15]/table/tbody/tr[2]/td/label")
driver.execute_script("arguments[0].scrollIntoView();", male)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys()
