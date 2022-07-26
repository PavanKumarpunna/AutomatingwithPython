from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")
'''
driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.implicitly_wait(30)

driver.switch_to.frame('iframeResult')
driver.find_element_by_xpath("//button[text()='Try it']").click()
time.sleep(5)
#driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()
Al = driver.switch_to.alert
print(Al.text)
Al.accept()

'''

driver.maximize_window()
driver.get("http://leafground.com/pages/Alert.html")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//button[text()='Prompt Box']").click()
Ale = driver.switch_to.alert
print(Ale.text)
time.sleep(5)
Ale.send_keys("Selenium Python Class")
Ale.accept()