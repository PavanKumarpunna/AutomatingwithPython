from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\Webdriver\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver_win32\chromedriver.exe")

driver.set_page_load_timeout(30)  # Url

driver.get("https://www.bankofamerica.com/")
driver.implicitly_wait(30)
driver.maximize_window()

act = ActionChains(driver)
time.sleep(3)
act.move_to_element(driver.find_element_by_xpath("//a[@id='visitBetterMoneyHabitsTabletUp']"))
time.sleep(3)
act.click()
act.perform()


'''
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(3)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath("//h3[text()='Utilities']"))
actions.perform()


driver.get("http://expedia.com/")
driver.maximize_window()
driver.implicitly_wait(30)

act = ActionChains(driver)
act.move_to_element(driver.find_element_by_name("phoneNumber"))
act.move_by_offset(1500,150)

act.perform()
time.sleep(2)

driver.get("https://www.snapdeal.com/")
driver.maximize_window()
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath("//li[@navindex='6']")) #Mens Fashion
time.sleep(5)
actions.move_to_element(driver.find_element_by_xpath('//*[@id="category6Data"]/div[1]/div/div/p[2]/a/span')) #Sports Shoe
time.sleep(5)

actions.click()
actions.perform()

'''
