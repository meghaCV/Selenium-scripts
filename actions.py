from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
username = driver.find_element_by_name("txtUsername")
username.send_keys("Admin")
pwd = driver.find_element_by_name("txtPassword")
pwd.send_keys("admin123")

driver.find_element_by_name("Submit").click()
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
um = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(um).move_to_element(users).click().perform()
