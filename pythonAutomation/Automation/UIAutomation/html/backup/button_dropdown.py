#coding=utf-8

from selenium import  webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from time import  sleep
import  os


dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('button_dropdown.html')
dr.get(file_path)

sleep(1)

#点击下拉菜单
dr.find_element_by_link_text('Info').click()

#找到dropdown-menu父元素
WebDriverWait(dr,10).until(lambda the_driver: the_driver.find_element_by_class_name('dropdown-menu').is_displayed())

#找到better than
menu = dr.find_element_by_class_name('dropdown-menu').find_element_by_link_text('better than')

menu.click()

sleep(3)

dr.quit()