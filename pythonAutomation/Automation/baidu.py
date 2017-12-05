'''
打开百度，搜索selenium关键字
'''

import time
from selenium import webdriver
driver=webdriver.Ie()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

