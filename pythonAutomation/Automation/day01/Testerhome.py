from selenium import webdriver
import time
#注册
driver=webdriver.Chrome()
driver.get("https://testerhome.com/")
driver.find_element_by_xpath("//html/body/div[1]/nav/div/ul[1]/li[1]/a").click()
time.sleep(5)
driver.find_element_by_id("user_login").send_keys("yangyan")
driver.find_element_by_id("user_name").send_keys("杨艳")
driver.find_element_by_id("user_email").send_keys("15221629532@163.com")
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_name("user[password_confirmation]").send_keys("123456")
time.sleep(8)
driver.find_element_by_name("commit").click()
driver.quit()

#login

# driver = webdriver.Chrome()
# driver.get("https://testerhome.com/")
# driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul[1]/li[2]/a').click()
# time.sleep(5)
# driver.find_element_by_name("user[login]").send_keys('yangyan')
# driver.find_element_by_name("user[password]").send_keys('123456')
# driver.find_element_by_name("user[remember_me]").click()
# driver.find_element_by_name("commit").submit()
# driver.quit()