# Basic Automation

from selenium import webdriver                   # Importing req libraries.
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")    # Opening browser driver of chrome.
driver.get("https://www.google.co.in")           # Open the Website to work on.

textbox = driver.find_element_by_name("q")       # Finding req ID/NAME from insect code.
textbox.send_keys("Python")                      # Add the Search term in parentheses.
textbox.send_keys(Keys.RETURN)                   # Automatic press Enter Button and search.

driver.close()                                 # Terminates the browser.
