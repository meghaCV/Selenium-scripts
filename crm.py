from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(
    executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://freecrm.com")
print(driver.title)
time.sleep(3)
search_bar = driver.find_element_by_xpath("/html/body/div[1]/header/div/nav/div[2]/div/div[2]/ul/a")
search_bar.click()
search_bar = driver.find_element_by_name("email")
search_bar.send_keys("megha.vin29@gmail.com")
search_bar = driver.find_element_by_name("password")
search_bar.send_keys("Amalone03")
time.sleep(1)
# login click
search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div/div[3]")
search_bar.click()
# calendar sidebar click
search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]")
search_bar = driver.find_element_by_xpath("//*[@id='main-nav']/a[2]/span")
search_bar.click()
time.sleep(1)
# arrow button
time.sleep(5)
for i in range(2):
    search_bar = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/span[1]/button[3]/i")
    search_bar.click()
# check for checkbox

'''search_bar = driver.find_element_by_xpath("//*[@id='ui']/div/div[2]/div[2]/div/div[2]/div/div[2]")
status = driver.find_element_by_name("calendar").is_selected()
print(status)

#status = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/label").click()
#status = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/label").is_selected()

#checkbox unclick
for i in range(20):
    try:
        search_bar = driver.find_element_by_xpath("//*[@id='ui']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/label")
        #driver.find_element_by_xpath(".//*[contains(text(),'content')]").click()

        status = driver.find_element_by_name("calendar")
        status.click()
        break
    except NoSuchElementException as e:
        print('retry')
        time.sleep(3)

else:
    print('test failed')

#driver.quit()'''


def remove_ticks_checkboxes():
    checkboxes = driver.find_element_by_xpath("//*[@class='content']/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]")
    for checkbox in checkboxes:
        if checkbox.is_selected == "True":  # If checkbox is ticked
            checkbox.click()
