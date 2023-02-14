import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


class SeleniumTestCase(unittest.TestCase):
    client = None

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.client = webdriver.Chrome(options=options)

        self.client.implicitly_wait(3)
        self.client.maximize_window()
        # time.sleep(3)

    def tearDown(self):
        # self.client.quit()
        self.client.close()

    def test_commscope1(self):
        client = self.client

        # 1 @todo Open browser in http://localhost:3000/shows
        client.get('http://localhost:3000/shows')

        # 2 @todo Enter a text in search box with text batman
        search_input = client.find_element_by_name('search')
        search_input.send_keys('batman')
        print('value of search input:', search_input.get_attribute('value'))

        # 3 @todo Press button search
        client.find_element_by_css_selector(
            'button.btn.waves-effect.waves-light').click()  # @todo change it by partial link text
        # @todo assert that the currrent url is http://localhost:3000/shows/search' current_url
        # @todo assert that the page contais the word results

        time.sleep(3)

        # 4 @todo Navigate to the url that is show in second card of results
        # results = client.find_elements_by_css_selector('div.row>div.col.s12>div.card.light-blue.darken-1>div.card-action.light-blue.darken-4>a.white-text')
        search_results = client.find_elements_by_css_selector('div.row>div.col.s12')
        second_card_link = search_results[1].find_element_by_link_text('URL')
        second_card_link.click()

        # @todo assert that the current url is the href of the link
        # print('results', len(search_results), second_card_link.get_attribute('href'))
        # print('link', results[1].get_attribute('href'))

        # 5 @todo Navigate back using browser features
        client.back()
        # @todo assert that the currrent url is http://localhost:3000/shows/search'

        # 6 @todo Change css background color to #4a148c to card with title Batman Unlimited
        wait = WebDriverWait(client, 5)
        card = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Batman Unlimited']//ancestor::div[contains(@class,'card')]")))

        #color_before = Color.from_string(card.value_of_css_property('background-color'))
        #print('color', color_before.hex)

        test_color = '#4a148c'
        client.execute_script("arguments[0].setAttribute('style', 'background-color: " + test_color + " !important')",
                              card)
        time.sleep(3)
        color_after = Color.from_string(card.value_of_css_property('background-color'))
        #print('color', color_after.hex)
        self.assertEqual(color_after.hex, test_color)

        # 7 @todo Press back button
        client.find_element_by_partial_link_text('BACK').click()
        time.sleep(3)

        # 8 @todo Make sure that input for search is empty
        search_input = client.find_element_by_name('search')
        self.assertEqual(search_input.get_attribute('value'), "")


if __name__ == "__main__":
    unittest.main()
