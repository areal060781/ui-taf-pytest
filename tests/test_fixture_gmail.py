import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    # options = ChromeOptions()
    # username = 'gc-gdl-lt45'
    # user_path = "/home/" + username + "/.config/google-chrome"
    # user_path = "/Users/" + username + "/Library/Application Support/Google/Chrome"
    # options.add_argument('--incognito')
    # options.add_argument("--user-data-dir="+user_path)
    # options.add_argument('--profile-directory=Profile 3')
    # driver = Chrome(options=options)
    driver = Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_open_first_email_and_get_subject_name(browser):
    try:
        url = 'https://mail.google.com'
        browser.get(url)
        browser.find_element_by_id('identifierId').send_keys('areal060781.dev@gmail.com')
        browser.find_element_by_id('identifierNext').click()
        time.sleep(5)

        browser.find_element_by_name('password').send_keys('B0n1F0nt')
        browser.find_element_by_id('passwordNext').click()
        time.sleep(10)

        first_mail = browser.find_element_by_xpath("//*[@class='yW']/span")
        first_mail.click()
        subject = browser.find_element_by_class_name('hP')
        print("Subject: ", subject.text)
        time.sleep(15)
    except Exception as e:
        print(e)
    finally:
        browser.close()
