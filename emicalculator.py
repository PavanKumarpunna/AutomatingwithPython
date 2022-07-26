import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications":2,
    "profile.default_content_setting_values.locations":2
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://sbi.co.in/web/student-platform/emi-calculator")
time.sleep(5)
amount = driver.find_element_by_xpath('//div[@id="loanamount_slider"]//span')
var = driver.find_element_by_xpath("//span[@style='left: 40%;']").location
print(var) # dict values
#accessing dict
print(var["x"])
# print(var.get("x"))
# print(var.get("y"))


action = ActionChains(driver)

#Either use drag and drop
#action.drag_and_drop_by_offset(amount,var["x"]//2,0)
#action.perform()
#
# #click and hold
action.move_to_element(amount)
action.click_and_hold().move_by_offset(98275/2,0).release().perform()

