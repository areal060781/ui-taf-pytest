import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTestCase(unittest.TestCase):
    client = None

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.client = webdriver.Chrome(options=options)

        self.client.maximize_window()
        self.client.implicitly_wait(5)

    def tearDown(self):
        # self.client.quit()
        self.client.close()

    def test_commscope1(self):
        """Write a Python3-Selenium script to load the webpage www.commscope.com and search for "ME-7000"
        Print the text for all the links found
        Submit the code and results obtained"""

        client = self.client

        client.get('https://www.commscope.com')

        self.assertTrue(re.search('Maximize your entire network', client.page_source))

        client.find_element_by_id("desktop-search-bar").send_keys('ME-7000', Keys.ENTER)
        client.implicitly_wait(3)
        time.sleep(3)
        self.assertTrue(re.search('Showing results for "ME-7000"', client.page_source))

        for link in client.find_elements_by_xpath("//a[contains(@class,'srch-link')]"):
            print(link.get_attribute("href"))

        self.assertTrue(re.search('1 results found', client.page_source))


if __name__ == "__main__":
    unittest.main()
