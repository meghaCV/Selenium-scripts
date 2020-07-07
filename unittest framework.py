import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/drivers for selenium/chromedriver-1")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")
