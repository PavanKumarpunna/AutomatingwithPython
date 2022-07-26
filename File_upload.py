from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications" : 2,
    "download.prompt_for_download" : False,
    "download.default_directory" : "C:\\Vignesh",

    }
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("http://www.leafground.com/pages/upload.html")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@name="filename"]').send_keys("C:\\Users\\Vignesh\\OneDrive\\Desktop\\FIle.txt")