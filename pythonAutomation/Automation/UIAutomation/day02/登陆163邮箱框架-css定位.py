#使用css定位，打开163邮箱

import time
from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import  ActionChains


class Email(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://mail.163.com/")
        self.driver.maximize_window()

    def test_email_search(self):
        driver=self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_id('lbNormal')).perform()
        driver.switch_to.frame("x-URS-iframe")
        time.sleep(2)
        driver.find_element_by_css_selector("[name='email']").send_keys('17768609406')
        driver.find_element_by_css_selector("[name='password']").send_keys('Wj07139865')
        driver.find_element_by_css_selector("[id='dologin']").click()
        time.sleep(3)
        #print(driver.title)        #打印出title
        self.assertIn("网易邮箱6.0版",driver.title)

    def tearDown(self):
           # self.driver.quit()
            pass

testunit=unittest.TestSuite()
testunit.addTest(Email("test_email_search"))
filepath='E:\\report.html'
fp=open(filepath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='登陆-测试报告',description='测试执行情况')
runner.run(testunit)
fp.close()

