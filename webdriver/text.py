# coding=utf-8
#text获取元素文本

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)

#id = cp元素的文本信息
data = driver.find_element_by_id("cp").text
print(data)
time.sleep(3)

driver.quit()
