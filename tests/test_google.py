import pytest
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com')
    assert "Google" == driver.title
