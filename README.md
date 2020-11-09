## Basic Testing Framework

Aa simple automation framework. Goals covered:

1. Design of Features & Scenarios.
2. Test Execution Report Structure.
3. Automation Layers Organization.
4. Handling of Test Data.
5. Quality of In-Code Documentation.
6. Code Reusability and Maintainability.

### Requirements
* Python 3.8
* Pipenv
* Allure command line
* Selenium webdriver, Chrome, Firefox

### Installation
```sh
pipenv install --dev
```

### Run testcase
On the project path
```sh
python -m pytest testcases/test_guest.py --alluredir=./results
allure serve ./results
```

