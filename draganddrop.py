from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element_by_class_name("demo-frame"))

drag = driver.find_element_by_id("draggable")
drop = driver.find_element_by_id("droppable")

act = ActionChains(driver)
#act.drag_and_drop_by_offset(drag,100,200)
act.drag_and_drop(drag,drop)
act.perform()