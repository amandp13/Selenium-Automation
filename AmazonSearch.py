# Basic Automation 3rd

from selenium import webdriver                   # Importing req libraries.
from selenium.webdriver.common.keys import Keys

user_input = input("Enter Product to be Searched: ")

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.amazon.in/")
search_element = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
search_element.send_keys(user_input)

search_button = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
search_button.click()


