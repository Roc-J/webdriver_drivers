# coding=utf-8

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.find_element_by_link_text('贴吧').click()

browser.quit()

# Partial link text定位
# 部分链接定位

browser.find_element_by_partial_link_text("贴").click()
#通过find_element_by_partial_link_text()函数，只用“贴”字，脚本一样找到了“贴吧”的链接

