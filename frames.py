from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[@title='Change Theme' and @onclick='retheme()']").click()

#switchto
#driver.switch_to.frame(0)
#driver.switch_to.frame("iframeResult")
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@frameborder="0"]'))
driver.find_element_by_xpath("//button[text()='Try it']").click()
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.parent_frame()
driver.find_element_by_xpath("//a[@title='Change Theme' and @onclick='retheme()']").click()