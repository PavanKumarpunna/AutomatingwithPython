from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.naukri.com/")
driver.implicitly_wait(30)
time.sleep(10)
driver.find_element_by_id("block").click()
act = ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//div[text()='Tools']"))
act.move_to_element(driver.find_element_by_xpath("//a[text()='People Flow (β)']"))
#act.click()

act.perform()