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
#driver.maximize_window()

#driver.find_element_by_xpath("//a[@onclick='retheme()']").click()
#id/name
#driver.switch_to.frame("iframeResult")
#index
#driver.switch_to.frame(0)
#locators
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@frameborder="0"]'))

driver.find_element_by_xpath("//button[text()='Try it']").click()

#driver.switch_to.alert.accept()
driver.switch_to.alert.send_keys("Vijay")
driver.switch_to.alert.accept()
#driver.switch_to.default_content()
driver.switch_to.parent_frame()
driver.find_element_by_id('tryhome').click()
print(driver.current_url)