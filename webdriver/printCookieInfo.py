# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

#获得cookie信息
cookie = driver.get_cookies()

#打印cookie信息
print(cookie)
