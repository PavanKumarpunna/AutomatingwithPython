import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/Webdriver/chromedriver.exe")
driver.maximize_window()
driver.get("https://signup.mail.com/#.1258-header-signup2-1")
time.sleep(5)
domaincheck = Select(driver.find_element_by_xpath("//select[@formcontrolname='emailDomain']"))
#domaincheck.select_by_index(3)
domaincheck.select_by_value("asia.com")
time.sleep(5)
domaincheck.select_by_visible_text(" @engineer.com ")
#domaincheck.deselect_by_visible_text(" @engineer.com ")
print(domaincheck.__hash__())