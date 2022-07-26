from selenium import webdriver
import time

from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.set_page_load_timeout(30)
'''
driver.get("https://sbi.co.in/web/student-platform/emi-calculator")
driver.implicitly_wait(30)
#time.sleep(5)
amount = driver.find_element_by_xpath("//div[@id='loanamount_slider']/span")
var = driver.find_element_by_xpath("//span[text()='1.25Cr']").location
print(var) #dict
print(var.get("x")) #var["x"]
print(var.get("y"))
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(amount,var.get("x")//2,0)
actions.perform()
'''

driver.get("https://emicalculator.net/")
driver.implicitly_wait(30)
amount_bar = driver.find_element_by_xpath('//div[@id="loanamountslider"]/span')
var = driver.find_element_by_xpath("//span[text()='125L']").location
print(var["x"])#var.get('x')
print(var['y'])
act = ActionChains(driver)
#act.drag_and_drop_by_offset(amount_bar,var["x"]//2,0)
#act.perform()
act.click_and_hold(amount_bar)
act.move_by_offset(var["x"]//2,0)
act.release()
act.perform()