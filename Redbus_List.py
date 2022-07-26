from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.redbus.in/")
#driver.maximize_window()

driver.find_element_by_id("src").send_keys("Hyd")
time.sleep(2)
srclist = driver.find_elements_by_xpath("//input[@id='src']/following-sibling::ul/li")
for s in srclist:
    print(s) #print all the drop down values
    if 'Airport' in s.text:
        s.click()
        break