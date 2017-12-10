import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://testerhome.com/")
driver.find_element_by_xpath("/html/body/div[1]/nav/div/ul[1]/li[1]/a").click()
driver.find_element_by_id("user_login").send_keys("yangyan")
driver.find_element_by_id("user_name").send_keys("杨艳")
driver.find_element_by_id("user_email").send_keys("15221629532@163.com")
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_id("user[password_confirmation]").send_keys("123456")
