import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications":2,
    "profile.default_content_setting_values.locations":2
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.collegeweeklive.com/go-signup/go-signup2")
time.sleep(5)

Select(driver.find_element_by_name("attendeeType")).select_by_visible_text("Student Looking for Graduate Degree")
time.sleep(2)
#driver.find_element_by_xpath('//div[@aria-label="Majors of Interest"]').click()
Agri = driver.find_element_by_xpath("//label[text()='Agriculture']")
Archi = driver.find_element_by_xpath("//label[text()='Architecture']")
Crimi = driver.find_element_by_xpath("//label[text()='Criminology']")

#Agri.click()
driver.execute_script("arguments[0].click();",Agri)
driver.execute_script("arguments[0].click();",Archi)
driver.execute_script("arguments[0].click();",Crimi)


#scrollBy - Scrolling by pixel value
driver.execute_script("window.scrollBy(0,-1000);") #width and height
#scrollTo - Scrolling to top/bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
