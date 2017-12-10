from selenium import  webdriver
import time

dr = webdriver.Chrome()
dr.get("http://baidu.com")
print(dr.current_url)
time.sleep(2)

dr.get("http://sogou.com")
print(dr.current_url)
time.sleep(2)

dr.back()
print(dr.current_url)
time.sleep(2)

dr.forward()
print(dr.current_url)

#dr.quit()
dr.close()
