#Alerts - popup

#Switchto

# accept - yes/ok - positive cases
# dismiss - no/cancel - negative cases
# text - to print alert texxt
# send keys - to input value in alert

from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
#driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
#driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")

driver.implicitly_wait(30)

#frame name/id
#frame index
#frame locators
driver.switch_to.frame(0)
#driver.switch_to.frame("iframeResult")
#driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@name='iframeResult']"))
driver.find_element_by_xpath("//button[text()='Try it']").click()

# accept - yes/ok - positive cases
# dismiss - no/cancel - negative cases
# text - to print alert texxt
# send keys - to input value in alert
time.sleep(5)
print(driver.switch_to.alert.text)

#driver.switch_to.alert.dismiss()
#driver.switch_to.alert.accept()
driver.switch_to.alert.send_keys("Selenium Popup")
driver.switch_to.alert.accept()





