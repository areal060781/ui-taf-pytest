import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def test_drive():
    opts = Options()
    opts.headless = False
    # assert opts.headless

    browser = Firefox(options=opts)
    browser.implicitly_wait(3)

    browser.get('https://duckduckgo.com')

    search_form = browser.find_element_by_id('search_form_input_homepage')
    search_form.send_keys('real python')
    search_form.submit()

    time.sleep(3)

    results = browser.find_elements_by_class_name('result')

    print(results[0].text)

    browser.close()
    quit()
