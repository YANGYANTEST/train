import time
from selenium import webdriver
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()    #窗口最大化
driver.find_element_by_name("tj_trnews").click()
driver.find_element_by_xpath('//*[@id="ww"]').send_keys("selenium")
driver.find_element_by_xpath('//*[@id="sugarea"]/span[2]/input').submit()
driver.find_element_by_id("kw").clear()
driver.save_screenshot("baidu.png")#截取图片
time.sleep(3)
driver.quit()