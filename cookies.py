from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.amazon.in/")
print(driver.title)

cookies = driver.get_cookies()
print(len(cookies))

print(cookies)

cookie = {'name': 'Mickie', 'value': '278393'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))

print(cookies)

driver.delete_cookie('Mickie')
cookies = driver.get_cookies()
print(len(cookies))

print(cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

print(cookies)