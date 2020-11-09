from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .basescreen import BaseScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, driver):
        self.driver = driver
        self.best_seller_ebook_carousel = WebDriverWait(self.driver.instance, 10).until(
            ec.visibility_of_element_located((
                By.CLASS_NAME, "desktop-gateway-btf_BestSellersEbooksStrategy")))

        #self.best_seller_ebook_carousel = self.driver.instance\
         #   .find_element_by_class_name('desktop-gateway-btf_BestSellersEbooksStrategy')

    def validate_best_seller_ebook_carousel_is_visible(self):
        self.best_seller_ebook_carousel.is_displayed()
