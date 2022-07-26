from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.naukri.com/")
driver.implicitly_wait(30)

parentwin = driver.current_window_handle
allwin = driver.window_handles

for a in allwin:
    if a != parentwin:
        driver.switch_to.window(a)
        print(driver.current_url)

