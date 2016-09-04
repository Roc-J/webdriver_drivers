# get_attribute.py
# coding=utf-8

select = driver.find_element_by_tag_name("select")
allOptions = select.find_element_by_tag_name("option")
for option in allOptions:
	print("Value is:" + option.get_attribute('value'))
	option.click()
	