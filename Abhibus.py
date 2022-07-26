from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\Webdriver\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver_win32\chromedriver.exe")

driver.set_page_load_timeout(30)  # Url

driver.get("https://www.abhibus.com/")
time.sleep(3)
driver.find_element_by_class_name("popup-close").click()
driver.find_element_by_id("datepicker1").click()
time.sleep(3)

date = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr/td/a') # 18- 30
for d in date:
    if d.text == '29':
        d.click()