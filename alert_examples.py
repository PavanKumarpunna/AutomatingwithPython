from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome (executable_path="D:\Webdriver\chromedriver.exe")
'''

#Example 1 - Simple Alert
driver.set_page_load_timeout(45)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.implicitly_wait(30)
driver.maximize_window()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept() # click on Ok, Yes,

'''

#Example 2 - Confirmation Alert
'''
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
driver.implicitly_wait(30)
driver.maximize_window()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(5)
#driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()
'''

# Example 3 Prompt Alert

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.implicitly_wait(30)
driver.maximize_window()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(2)

print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Shaikat")
driver.switch_to.alert.accept()
