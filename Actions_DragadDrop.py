from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
source = driver.find_element_by_id('draggable')
dest = driver.find_element_by_id('droppable')
time.sleep(5)
action = ActionChains(driver)
action.drag_and_drop(source,dest)
action.perform()
