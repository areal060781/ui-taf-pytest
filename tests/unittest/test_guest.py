import unittest
from webdriver import Driver

from values import strings
from pageobjects.welcomescreen import WelcomeScreen
from pageobjects.cartscreen import CartScreen
from pageobjects.signinscreen import SignInScreen


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.instance.maximize_window()
        self.driver.navigate(strings.base_url)

    def test_welcome_screen_components(self):
        welcome_screen = WelcomeScreen(self.driver)
        welcome_screen.validate_title_is_present()
        welcome_screen.validate_nav_bar_is_visible()
        welcome_screen.validate_page_content_is_visible()
        welcome_screen.validate_best_seller_ebook_carousel_is_visible()
        welcome_screen.validate_nav_footer_is_visible()
        welcome_screen.validate_footer_links_are_present()

    def test_cart_screen_components(self):
        welcome_screen = WelcomeScreen(self.driver)
        welcome_screen.click_cart()

        cart_screen = CartScreen(self.driver)
        cart_screen.validate_right_bar_is_visible()
        cart_screen.validate_active_cart_is_visible()
        cart_screen.validate_sign_in_is_visible()

    def test_orders_screen_components(self):
        welcome_screen = WelcomeScreen(self.driver)
        welcome_screen.click_orders()

        sign_in_screen = SignInScreen(self.driver)
        sign_in_screen.validate_url()

    def tearDown(self):
        self.driver.instance.quit()

    if __name__ == '__main__':
        unittest.main()
