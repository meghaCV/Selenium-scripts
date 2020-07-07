from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://seleniumhq.github.io/selenium/docs/api/java/index.html")
print(driver.title)
#first frame
driver.switch_to.frame("packageListFrame")
driver.find_element_by_partial_link_text("org.openqa.selenium").click()
driver.switch_to.default_content()
time.sleep(2)
#second frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_partial_link_text("WebDriver").click()
driver.switch_to.default_content()
time.sleep(2)
#third frame
driver.switch_to.frame("classFrame")
links =driver.find_elements_by_class_name("navList")
print(len(links))

for link in links:
    print(link.text)

driver.find_element_by_xpath("/html/body/div[1]/ul/li[6]/a").click()
time.sleep(2)


