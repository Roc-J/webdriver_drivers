# coding = utf-8

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
driver.get('http://www.baidu.com')

time.sleep(3)
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
