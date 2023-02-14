# This sample uses pytest-selenium plugin

# Navigate to the URL https://lambdatest.github.io/sample-todo-app/
# Select the first two checkboxes
# Send ‘Happy Testing at LambdaTest’ to the textbox with id = sampletodotext
# Click the Add Button and verify whether the text has been added or not

# https://pytest-selenium.readthedocs.io/en/latest/
# pytest tests/test_pytest_selenium_plugin.py --driver Firefox

import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test_lambda_test_todo_app(selenium):
    selenium.get('https://lambdatest.github.io/sample-todo-app/')

    assert "Sample page - lambdatest.com" == selenium.title

    selenium.find_element_by_name('li1').click()
    selenium.find_element_by_name('li2').click()

    input_text = 'Happy Testing at LambdaTest'
    selenium.find_element_by_id('sampletodotext').send_keys(input_text)

    selenium.find_element_by_id('addbutton').click()

    last_li_text = selenium.find_element_by_css_selector('ul.list-unstyled>li:last-child>span').text
    assert last_li_text == input_text
