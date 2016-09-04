# lastcheckbox.py
#

from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

#选择所有的checkbox并全部勾选上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
	checkbox.click()
time.sleep(2)

#把页面上最后一个checkbox的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)

dr.quit()