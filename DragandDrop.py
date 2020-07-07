from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
print(driver.title)
src_element = driver.find_element_by_id("DHTMLgoodies_dragableElement2")
trt_element = driver.find_element_by_id("box103")

actions = ActionChains(driver)
actions.drag_and_drop(src_element, trt_element).perform()