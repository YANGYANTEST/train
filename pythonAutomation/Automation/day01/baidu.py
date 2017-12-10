'''
打开百度，搜索selenium关键字
'''
import time
from selenium import webdriver
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()    #窗口最大化
driver.refresh()
time.sleep(5)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

