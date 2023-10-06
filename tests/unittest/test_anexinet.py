import unittest
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AnexinetTestCase(unittest.TestCase):
    def setUp(self):
        #options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #self.driver = webdriver.Chrome(options=options)

        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    def test_admin_home_page(self):
        driver = self.driver

        # navigate to home page
        driver.get('https://anexinet.com/')

        self.assertTrue(re.search('Anexinet\s+Corp.,', driver.page_source))

        # navigate to login page
        # contact_link = WebDriverWait(driver, 5).until(
        #     ec.element_to_be_clickable((
        #         By.CSS_SELECTOR, "a.linkmenu.a-level-0")))
        # contact_link.click()

        #driver.find_element_by_css_selector("a.linkmenu.a-level-0").click()
        #driver.find_element_by_xpath("//a[contains(@href,'contact-us')]").click()
        #driver.find_element_by_link_text('CONTACT').click()



        # contact_link = WebDriverWait(driver, 20).until(
        #     ec.presence_of_element_located((By.XPATH, "//a[contains(@href,'contact-us')]")))
        # driver.implicitly_wait(2)
        # contact_link.click()




        #self.assertIn("<span>Let's Get Started</span>", driver.page_source)
        #
        # # contact info form
        # driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys('Aida Real')
        # driver.find_element_by_name('email').send_keys('john@example.com')
        # driver.find_element_by_name('password').send_keys('cat')
        # driver.find_element_by_name('submit').click()
        # self.assertTrue(re.search('Hello,\s+john!', driver.page_source))
        #
        # # navigate to the user's profile page
        # driver.find_element_by_link_text('Profile').click()
        # self.assertIn('<h1>john</h1>', driver.page_source)


if __name__ == "__main__":
    unittest.main()
