from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.set_page_load_timeout(30)#30 - seconds
driver.get("https://www.irctc.co.in/nget/train-search")
driver.implicitly_wait(30) #sec
#driver.find_element_by_xpath("//button[text()='Okay']").click()

wait= WebDriverWait(driver,15)
ele = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Ok']")))
driver.find_element_by_xpath("//button[text()='Ok']").click()