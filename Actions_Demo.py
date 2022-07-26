from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.implicitly_wait(30)

act = ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//span[text() = 'Mobile & Tablets']"))
act.move_to_element(driver.find_element_by_xpath("//span[text()='Panasonic']"))
act.click()
time.sleep(2)
act.move_to_element(driver.find_element_by_xpath("//input[@placeholder='Your email address']"))
act.send_keys("test@gmail.com")
act.perform()


