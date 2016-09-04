# mousedrag.py
# coding=utf-8

#定位元素的原位置
element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
target = driver.find_element_by_name('target')

#执行元素的移动操作
ActionChains(driver).drag_and_drop(element,target).perform()
