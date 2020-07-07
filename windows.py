from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Sakinalium | Home":
       driver.close()

#driver.quit()


