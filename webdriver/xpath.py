#xpath:attributer (属性)
driver.find_element_by_xpath("//input[@id='kw']").send_keys("seleninum")
#input标签下id = kw 的元素

#xpath:idRelative(id相关性)
driver.find_element_by_xpath("//div[@id='fm']/form/sapn/input").send_keys('seleninum')

#在/form/span/input层级标签下有个div标签的id=fm的元素

driver.find_element_by_xpath("//tr[@id='check']/td[2]").click()

#id为'check'的tr,定位它里卖弄的第2个td

#xpath:position(位置)
driver.find_element_by_xpath("//input").send_keys("seleninum")
driver.find_element_by_xpath("//tr[7]/td[2]").click()
#第七个tr里面的第二个td

xpath:href(水平参考)
driver.find_element_by_xpath("//a[contain(text(),'网页')]").click()
#在a标签下有个文本(text)包含(contains)'网页'的元素

xpath:link
driver.find_element_by_xpath("//a[@href]='http://www.baidu.com/'").click()

#有个叫a的标签，他有个链接href='http://www.baidu.com/'的元素
