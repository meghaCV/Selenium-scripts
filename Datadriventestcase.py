from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import XLUtils
import openpyxl

driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")
print(driver.title)

path = "/Users/chandrashekarbasavaraj/Downloads/DDT.xlsx"
workbook1 = openpyxl.load_workbook(path)
sheet = workbook1.active
print(workbook1.sheetnames)

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    # reading data from excel to application
    name = XLUtils.readData(path, "Sheet1", r, 1)
    pwd = XLUtils.readData(path, "Sheet1", r, 2)
    driver.find_element_by_name("userName").send_keys(name)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_name("login").click()

    if driver.title =="Welcome:Mercury Tours":
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")

    else:
        print("Test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element_by_partial_link_text("Home").click()
