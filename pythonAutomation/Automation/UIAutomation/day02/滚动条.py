from selenium import webdriver
import  time
timepic=time.strftime("%Y-%m-%d-%H_%M_%S")
dr1=webdriver.Chrome()
dr1.get("https://shanghai.anjuke.com/")
dr1.implicitly_wait(5)
dr1.execute_script('var q=document.documentElement.scrollTop=10000')
dr1.save_screenshot("E:\train\PycharmProjects\train\pythonAutomation\Automation\picture"+timepic+".png")
time.sleep(10)
dr1.quit()