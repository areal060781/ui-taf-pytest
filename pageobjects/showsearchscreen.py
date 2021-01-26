class ShowSearchScreen:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = driver.find_element_by_name('search')
        #self.search_button = driver.find_element_by_css_selector(
        #   'button.btn.waves-effect.waves-light')  # @todo change it by partial link text
        self.search_button = driver.find_element_by_partial_link_text('Search')
        self.search_results = driver.find_elements_by_css_selector('div.row>div.col.s12')

    def run(self, text):
        self.search_input.send_keys(text)
        self.search_button.click()

        assert self.driver.current_url == self.RESULTS_URL

    def validate_input_search_is_empty(self):
        search_input = self.driver.find_element_by_name('search')

        assert search_input.get_attribute('value') == ""
