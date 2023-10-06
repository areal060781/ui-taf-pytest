from selenium import webdriver


def test_safari_browser():
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver = webdriver.Safari()
    driver.get("https://www.damien.co")
    driver.quit()
