import pytest
import os
from appium import webdriver


@pytest.fixture(scope="function")
def driver():
    # 'app': os.path.expanduser('./android/app/build/outputs/apk/app-debug.apk'),
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'GS8',
            'appPackage': 'com.grainchain.forms',
            'appActivity': 'com.grainchain.forms.MainActivity',
            'udid':'3653354b4c303098'
        })

    yield driver  # Test code runs after this line

    # Teardown
    driver.quit()
