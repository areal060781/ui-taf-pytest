from selenium import webdriver
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Safari()
driver.get("https://www.damien.co")
driver.quit()