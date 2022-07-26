import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import datetime
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications":2,
    "profile.default_content_setting_values.locations":2
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.redbus.in/")
time.sleep(5)
'''
#scrollintoview - to specific position
AllOperators =  driver.find_element_by_xpath("//div[text()=' We promise to deliver']")
driver.execute_script("arguments[0].scrollIntoView(true);",AllOperators)
'''
currentsec = datetime.datetime.now().strftime("%b"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%f")
''
driver.save_screenshot("C:\\Vignesh\\redbus"+currentsec+".png")
driver.get_screenshot_as_png()# it has having issue
driver.get_screenshot_as_file("redbus"+currentsec+".png")
driver.get_screenshot_as_base64()