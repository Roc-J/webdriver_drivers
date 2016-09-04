# coding = utf-8
#<input class="b_searchbox" id="sb_form_q" name="q" title="输入搜索词" type="search" value="" maxlength="100" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" role="combobox" aria-autocomplete="both" aria-expanded="false" aria-owns="sa_ul">

from seleninum import webdriver
browser = webdriver.Chrome()

browser.get('http://cn.bing.com')

##########必应输入框的定位方式###########

#通过id方式定位
browser.find_element_by_id('sb_form_q').send_keys('seleninum')

#通过name方式定位
browser.find_element_by_name('q').send_keys('seleninum')

#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys('seleninum')

#通过class name方式定位
browser.find_element_by_class_name("b_searchbox").send_keys('seleninum')

#通过CSS方式定位
browser.find_element_by_css_selector('#b_searchbox').send_keys('seleninum')

#通过xpath方式定位
browser.find_element_by_xpath('//input[@id="sb_form_q"]').send_keys('seleninum')


###################################
browser.find_element_by_id('sb_form_go').click()

time.sleep(5)

browser.quit()

#<a href="http://news.baidu.com" name="tj_news">新闻</a>
#driver.find_element_by_css_selector("a[name='tj_news']").click()

#<a onclick="queryTab(this);" mon="col=502&pn=0" title="web" href="http://www.baidu.com/">网页</a>

driver.find_element_by_css_selector('a[title="web"]').click()

#<a class="RecycleBin xz" href="javascript:void(0);">

driver.find_element_by_css_selector('a.RecycleBin').click()

