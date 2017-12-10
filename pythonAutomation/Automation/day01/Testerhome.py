from selenium import webdriver
import time

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
# driver.find_element_by_name("commit").click() #点击提交注册信息
driver.find_element_by_xpath('//*[@id="new_user"]/div[8]/a').click()    #点击登陆
# driver.quit()
time.sleep(5)

#login

driver=webdriver.Chrome()
driver.get("https://testerhome.com/")
driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul[1]/li[2]/a').click()
time.sleep(5)
driver.find_element_by_name("user[login]").send_keys('yangyan')
driver.find_element_by_name("user[password]").send_keys('123456')
# driver.find_element_by_name("user[remember_me]").click()
driver.find_element_by_name("commit").submit()
time.sleep(3)
# driver.quit()
driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[3]').click()


