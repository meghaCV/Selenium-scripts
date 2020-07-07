from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScxBZFFOR4fyIySJEEV8_Yrn0XJZgiR-SxISdPLr2gD9ktFZQ/viewform")
print(driver.title)

driver.execute_script("window.scrollBy(0,500)", "")
input = driver.find_elements(By.CLASS_NAME, 'ss-q-short required')

ct = len(input)
print(ct)

name = driver.find_element_by_name("entry.1228038601")
name.send_keys("Megha")

contact = driver.find_element_by_name("entry.1654717672")
contact.send_keys("megha.vin28@gmail.com")

phno = driver.find_element_by_name("entry.1867142824")
phno.send_keys("076453892")

'''mrngchk = driver.find_element_by_name("entry.41135172")
print(mrngchk.is_displayed())
if mrngchk.is_displayed():
   mrngchk.click()
else:
   print("failed")'''

wait = WebDriverWait(driver, 10)
mrngchk = wait.until(EC.element_to_be_clickable((By.NAME, "entry.41135172")))

#mrngchk = driver.find_element_by_name("entry.41135172")
mrngchk.click()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
DC = driver.find_element_by_name("entry.954097784")
print("status of DC is", DC.is_selected())
DC.click()
print("status of DC is", DC.is_selected())

element = driver.find_element_by_id("entry_618389072")
drp = Select(element)

#select by visible text
#drp.select_by_index(3)
time.sleep(2)


#select by visible text
drp.select_by_visible_text('XXL')


#count the no of options
print("The no of options are", len(drp.options))

#capture all the options in drp
all_options = drp.options

for option in all_options:
    print("Options are as below", option.text)