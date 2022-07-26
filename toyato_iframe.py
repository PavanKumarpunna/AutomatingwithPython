from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.toyota.co.uk/order-a-brochure")
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Yes, I agree']").click()
time.sleep(2)
driver.switch_to.frame(1)
#driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@type="responsive-iframe"]'))

driver.find_element_by_xpath("//div[text()='Download']").click()