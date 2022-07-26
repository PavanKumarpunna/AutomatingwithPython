## Java script executor

from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.irctc.co.in/nget/")
driver.implicitly_wait(30)


pnrstatus = driver.find_element_by_xpath("//label[text()='PNR STATUS']")
#driver.execute_script("arguments[0].click();",pnrstatus)
pnrstatus.click()
