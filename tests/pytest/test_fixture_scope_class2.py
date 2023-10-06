import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture(scope="class")
def chrome_driver(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver")
class BasicChromeTest:
    pass


class Test_URL_Chrome(BasicChromeTest):
    def test_google_url_title(self):
        self.driver.get("https://www.google.com/")
        assert "Google" == self.driver.title
        sleep(5)

    def test_facebook_uri_title(self):
        self.driver.get("https://www.facebook.com/")
        assert "Facebook - Log In or Sign Up" == self.driver.title
        sleep(5)
