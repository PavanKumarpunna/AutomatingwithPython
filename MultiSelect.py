import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/Webdriver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
time.sleep(5)
driver.switch_to.frame("iframeResult")

car = Select(driver.find_element_by_id("cars"))
car.select_by_value("volvo")
car.select_by_value("opel")
