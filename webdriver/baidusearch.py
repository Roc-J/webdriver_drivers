# 该脚本不能执行，执行报错

from selenium import webdriver
import os,time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#进入搜索设置页
driver.find_element_by_link_text('搜索设置').click()

#设置每页搜索结果为100条
m = driver.find_element_by_name('NR')
m.find_element_by_xpath("//option[@value='50']").click()
time.sleep(3)

#保持设置的信息
driver.find_element_by_xpath("//input[@value='保存设置']").click()
time.sleep(3)
driver.switch_to_alert().accept()

#跳转到百度首页后，进行搜索表
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

driver.quit()