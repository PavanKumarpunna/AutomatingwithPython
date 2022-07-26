from selenium import webdriver
from selenium.webdriver.support.ui import Select


def Selectdropdown(xpath, value):
    x = driver.find_element_by_xpath(xpath)
    Select(x).select_by_visible_text(value)


driver = webdriver.Chrome()
driver.get("https://signup.mail.com/#.1258-header-signup2-1")
driver.maximize_window()

emailDomain = driver.find_element_by_xpath('//select[@formcontrolname="emailDomain"]')
#Select(emailDomain).select_by_value("asia.com")
#Select(emailDomain).select_by_index(15)
Select(emailDomain).select_by_visible_text(" @computer4u.com ")

#Selectdropdown('//select[@data-test="country-input"]',"India")
alloptions = Select(emailDomain).options

print(len(alloptions))
for s in alloptions:
    print(s.text)