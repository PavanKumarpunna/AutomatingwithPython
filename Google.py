from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/Webdriver/chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()

'''
driver.find_element_by_name("email").send_keys("User1")
driver.find_element_by_id("pass").send_keys("pass")
driver.find_element_by_id("loginbutton").click()
'''

driver.find_element_by_xpath("//input[@aria-label='First name']").send_keys("Python")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Selenium")
driver.find_element_by_xpath("//input[contains(@aria-label,'Mobile number or ')]").send_keys("99418569872")

driver.find_element_by_xpath("//*[text()='Sign Up' and @name='websubmit']").click()