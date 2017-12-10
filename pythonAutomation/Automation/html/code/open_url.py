
from selenium import webdriver
import time


dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
print(dr.title)


dr.close()