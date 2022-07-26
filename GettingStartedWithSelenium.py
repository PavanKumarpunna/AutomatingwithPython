from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://www.facebook.com/")
driver.find_element_by_name("email").send_keys("user1@gmail.com")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_name("login").click()
time.sleep(5)
driver.find_element_by_partial_link_text("Forgotten").click()