import pytest
from selenium import webdriver
import time


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicChromeTest:
    pass


class Test_URL_Chrome(BasicChromeTest):
    @pytest.mark.parametrize('url', ['https://www.google.com/'])
    def test_google_url_title(self, url):
        self.driver.get(url)
        assert 'Google' == self.driver.title
        time.sleep(5)
