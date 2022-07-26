import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/Webdriver/chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(50)
driver.get("https://www.irctc.co.in/nget/train-search")
#driver.get("https://www.abhibus.com/")
driver.implicitly_wait(30)
#driver.find_element_by_link_text("Trains").click()
wait = WebDriverWait(driver,15)
#driver.find_element_by_xpath("//button[text()='Ok']").click()
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Ok']")))
driver.find_element_by_xpath("//button[text()='Ok']").click()