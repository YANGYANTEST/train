from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()
file_path="file:///C:/Users/15221/Desktop/python/20171210/html/html/code/form.html"
print(file_path)

dr.get(file_path)

#by id
dr.find_element_by_id("inputEmail").click()

#by nane
dr.find_element_by_name('password').click()

#by tagname
print(dr.f)