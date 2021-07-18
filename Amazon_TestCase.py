# Basic Automation Test cases 4th

import unittest
from selenium import webdriver  # Importing req libraries.
# from selenium.webdriver.common.keys import Keys


class SearchText(unittest.TestCase):
    # Inherit Testcase class
    def setUp(self) -> None:  # All Setup done are called.
        self.user_input = input("Enter Product to be Searched: ")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.amazon.in/")

    def test_search_results(self):
        search_element = self.driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
        search_element.send_keys(self.user_input)

        search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
        search_button.click()

        # To check the test case when search result shows 16 results or not.

        elements = self.driver.find_elements_by_xpath("//*[@data-component-type='s-search-result']")
        # print(len(elements))
        self.assertEqual(16, len(elements))
        # It fails as AD makes it 18.


if __name__ == '__main__':
    unittest.main()
