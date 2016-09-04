# coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('upload_file.html')
driver.get(file_path)

#定位上传按钮，添加本地文件
path = os.path.abspath('upload_file.txt')
driver.find_element_by_name('file').send_keys(path)
time.sleep(2)
driver.quit()
