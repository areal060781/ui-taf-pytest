import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseScreen:
    @allure.step("Validate Page Title is present")
    def validate_title_is_present(self):
        title = self.driver.instance.title
        assert "Amazon.com.mx:" in title

    def validate_nav_bar_is_visible(self):
        nav_bar = self.driver.instance.find_element_by_id('navbar')
        assert nav_bar.is_displayed()

    def validate_page_content_is_visible(self):
        page_content = self.driver.instance.find_element_by_id('pageContent')
        assert page_content.is_displayed()

    def validate_nav_footer_is_visible(self):
        nav_footer = self.driver.instance.find_element_by_id('navFooter')
        assert nav_footer.is_displayed()

    def validate_footer_links_are_present(self):
        nav_footer = self.driver.instance.find_element_by_id('navFooter')
        footer_links = nav_footer.find_elements_by_xpath("//a[contains(@class,'nav_a')]")
        assert len(footer_links) > 0

    @allure.step("Click Cart menu link")
    def click_cart(self):
        cart_menu = self.driver.instance.find_element_by_id('nav-cart')
        cart_menu.click()
        current_url = self.driver.instance.current_url
        assert "nav_cart" in current_url

    @allure.step("Click Orders menu link")
    def click_orders(self):
        orders_menu = self.driver.instance.find_element_by_id('nav-orders')
        orders_menu.click()
