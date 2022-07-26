import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:/Webdriver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.openmultipleurl.com/")
time.sleep(5)

driver.find_element_by_name("list_urls").send_keys("https://www.bing.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.google.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.facebook.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.amazon.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.yahoo.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.ebay.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)

driver.find_element_by_id("button").click()

#############################################

print(driver.title)
print(driver.current_url)

parentwindow = driver.current_window_handle
print(parentwindow)

allopenwindows = driver.window_handles
print(len(allopenwindows))
print(type(allopenwindows))

for a in allopenwindows:
    print(a)
    if a != parentwindow:
        driver.switch_to.window(a)
        #time.sleep(8)
        print(driver.title)
        print(driver.current_url)
        if "Google" in driver.title:
            print("Google")
            break

        else:
            driver.close()

print(driver.current_url)