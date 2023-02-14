# Navigate to the URL https://lambdatest.github.io/sample-todo-app/
# Select the first two checkboxes
# Send ‘Happy Testing at LambdaTest’ to the textbox with id = sampletodotext
# Click the Add Button and verify whether the text has been added or not

import pytest
from selenium import webdriver


def test_lambda_test_todo_app():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://lambdatest.github.io/sample-todo-app/')

    assert "Sample page - lambdatest.com" == driver.title

    driver.find_element_by_name('li1').click()
    driver.find_element_by_name('li2').click()

    input_text = 'Happy Testing at LambdaTest'
    driver.find_element_by_id('sampletodotext').send_keys(input_text)

    driver.find_element_by_id('addbutton').click()

    last_li_text = driver.find_element_by_css_selector('ul.list-unstyled>li:last-child>span').text
    assert last_li_text == input_text

    driver.close()
