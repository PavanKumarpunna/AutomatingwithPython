## Java script executor

from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

#scrolling down
driver.execute_script("window.scrollBy(0,1000);") #width,height
#Scroll up
driver.execute_script("window.scrollBy(0,-1000);") #width,height

#scrollto - to scroll to end of the pagee

driver.execute_script("window.scrollTo(document.body.scrollWidth,document.body.scrollHeight);")

#to scroll up
driver.execute_script("window.scrollTo(-document.body.scrollWidth,-document.body.scrollHeight);")

###############
#scrollintoview
growingwebelement = driver.find_element_by_xpath('//div[contains(text(),"The numbers are growing!")]')
driver.execute_script("arguments[0].scrollIntoView(true);",growingwebelement)