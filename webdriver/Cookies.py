# Cookies.py
#

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

#向cookie的name和value添加会话信息
driver.add_cookie({'name':'qjk','value':'Roc-J'})

#遍历
for cookie in driver.get_cookies():
	print("%s -> %s" % (cookie['name'],cookie['value']))
print('*****************')
#删除特定的
driver.delete_cookie('qjk')
for cookie in driver.get_cookies():
	print("%s -> %s" % (cookie['name'],cookie['value']))
print('*****************')
#删除所有的cookie
driver.delete_all_cookies()
for cookie in driver.get_cookies():
	print("%s -> %s" % (cookie['name'],cookie['value']))

time.sleep(3)
driver.close()