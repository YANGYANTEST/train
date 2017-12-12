import time
from selenium import webdriver
dr=webdriver.Chrome()
dr.get("http://www.baidu.com")
print(dr.current_url)#打印当前的url

time.sleep(3)
dr.get("http://sougou.com")
print(dr.current_url)
dr.forward()#前进
time.sleep(2)
dr.back()#往后
dr.close()#关闭


