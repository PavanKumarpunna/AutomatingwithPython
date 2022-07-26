from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\Webdriver\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

driver.find_element_by_id("twotabsearchtextbox").send_keys("Batman toy")
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit' and @value='Go']").click()

driver.find_element_by_xpath("//span[@data-component-id='9']/a").click()

parent_window = driver.current_window_handle # primary window which we are in before launching the sub windows
handle = driver.window_handles # to store the number of windows. it will be stored as set
print(len(handle))

for h in handle:
    if h != parent_window:
        driver.switch_to.window(h)
        print(driver.current_url)
       # driver.find_element_by_class_name("a-button-text a-text-left").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[@id='wishListMainButton-announce']").click()

        time.sleep(3)
        driver.find_element_by_id("ap_email").send_keys("9941625522")
        driver.find_element_by_id("continue").click()