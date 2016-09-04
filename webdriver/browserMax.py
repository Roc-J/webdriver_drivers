# browserMax.py
# coding = utf-8

from selenium import webdriver
from Function import *
import time

browser = webdriver.Chrome()
browser.get('http://baidu.com')

# print("浏览器最大化")
# browser.maximize_window() #将浏览器最大化显示
# time.sleep(2)
# print("设置浏览器宽480、高800显示")
# browser.set_window_size(480,800)

# browser.find_element_by_id('kw').send_keys('selenium')
#browser.find_element_by_id('su').click()
#browser.find_element_by_id('su').submit()
textLink(browser,"贴吧")
#browser.find_element_by_link_text("新闻").click()
time.sleep(3)

