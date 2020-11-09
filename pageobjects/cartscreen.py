from .basescreen import BaseScreen


class CartScreen(BaseScreen):
    def __init__(self, driver):
        self.driver = driver
        self.right_bar = self.driver.instance.find_element_by_id('sc-rec-right')
        self.active_cart = self.driver.instance.find_element_by_id('sc-active-cart')

    def validate_right_bar_is_visible(self):
        assert self.right_bar.is_displayed()

    def validate_active_cart_is_visible(self):
        assert self.active_cart.is_displayed()

    def validate_sign_in_is_visible(self):
        sign_in = self.driver.instance.find_element_by_css_selector('.sc-sign-in')
        assert sign_in.is_displayed()
