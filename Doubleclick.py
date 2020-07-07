from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
clickbutton = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(clickbutton).perform()