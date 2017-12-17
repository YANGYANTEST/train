'''
对某个网站自动注册账号，自动登陆账号，自动发个帖子，发完后自动截取一张，有时间的话，加一个自动将图片发到自己的邮箱
'''

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://118.31.19.120:3000/")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('Alina')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="re_pass"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('2214373539@qq.com')
driver.find_element_by_xpath('//*[@id="signup_form"]/div[5]/input').click()
driver.quit()



