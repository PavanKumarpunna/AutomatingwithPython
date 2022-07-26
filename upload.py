import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications":2,
    "profile.default_content_setting_values.locations":2,
    "download.prompt_for_download": False,
    "download.default_directory": "C:\\Vignesh",

}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)
#
# driver.get("http://www.leafground.com/pages/upload.html")
# time.sleep(5)
# driver.find_element_by_name("filename").send_keys("C:\\Users\\Vignesh\\OneDrive\\Desktop\\FIle.txt")

driver.get("http://www.leafground.com/pages/download.html")
time.sleep(5)
driver.find_element_by_link_text("Download Excel").click()
