from selenium import webdriver
import logging

logging.basicConfig(filename="/Users/chandrashekarbasavaraj/Downloads/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p',
                    level=logging.DEBUG)
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
