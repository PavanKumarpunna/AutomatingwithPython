from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://signup.mail.com/#.1258-header-signup2-1")
driver.implicitly_wait(30)

mailcategory = driver.find_elements_by_xpath('//select[@data-test="check-email-availability-email-domain-input"]//option')
for m in mailcategory:
    print(m.text)
    if "asia" in m.text:
        m.click()
        break