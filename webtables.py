from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import time

path = "/Users/chandrashekarbasavaraj/Downloads/Writedata.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.worldometers.info/coronavirus/")
print(driver.title)

report = driver.find_element_by_partial_link_text("Report coronavirus cases")
driver.execute_script("arguments[0].scrollIntoView();", report)

rows = len(driver.find_elements_by_xpath("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/thead/tr/th"))

print(rows)
print(cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value1 = driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr["+str(r)+"]/td["+str(c)+"]").text
        #print(value, end=' ')
        sheet.cell(row=r, column=c).value = value1
    print()

workbook.save(path)
