from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_experimental_option("prefs", {"download.default_directory": "/Users/chandrashekarbasavaraj/Documents"})
driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1", chrome_options=options)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")
print(driver.title)
ftb = driver.find_element_by_id("textbox")
ftb.send_keys("Manasvin")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

driver.find_element_by_id("pdfbox").send_keys("Megha")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
