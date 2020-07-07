from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.implicitly_wait(5)

usr_ele = driver.find_element_by_name("userName")
print(usr_ele.is_displayed())
print(usr_ele.is_enabled())
usr_ele.send_keys("mercury")

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
pwd_ele.send_keys("mercury")
sign = driver.find_element_by_name("login")
sign.click()

roundtrip_radiobutton = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of rt is",roundtrip_radiobutton.is_selected())

onetrip_radiobutton = driver.find_element_by_css_selector("input[value=oneway]")
print("status of ot is",onetrip_radiobutton.is_selected())
