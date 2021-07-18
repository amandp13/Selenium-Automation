# Basic Automation 2nd

from selenium import webdriver                   # Importing req libraries.
from selenium.webdriver.common.keys import Keys

url = "https://www.facebook.com/"
email = "shirleyvats@gmail.com"
password = "creatapassword."

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

emailTextBox = driver.find_element_by_id("email")
emailTextBox.send_keys(email)

passwordTextBox = driver.find_element_by_id("pass")
passwordTextBox.send_keys(password)

# We have multiple option as per the security of Website.

# button = driver.find_element_by_name("login")
# button.click()

# button = driver.find_element_by_xpath("//*[@id='u_0_j_fr']")
# button.click()

# Hit Enter asa password fills.
passwordTextBox.send_keys(Keys.ENTER)

driver.close()
