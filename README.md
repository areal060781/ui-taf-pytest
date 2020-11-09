## Basic Testing Framework

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

