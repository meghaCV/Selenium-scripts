from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
print(driver.title)

wait = WebDriverWait(driver, 10)
alert = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='HTML9']/div[1]/button")))
#driver.find_element_by_xpath()
alert.click()
time.sleep(5)
#driver.switch_to.alert().accept()
driver.switch_to.alert().dismiss()
driver.find_element_by_id("cookieChoiceDismiss").click()