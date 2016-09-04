# coding = utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://cn.bing.com')

browser.find_element_by_id('sb_form_q').send_keys('selenium')
browser.find_element_by_id('sb_form_go').click()

time.sleep(3)

browser.quit()