# coding = utf-8

form selenium import webdriver
import time 

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(1)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

time.sleep(3)
browser.quit()
