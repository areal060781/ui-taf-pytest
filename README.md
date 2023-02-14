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
python -m pytest tests/test_guest.py --alluredir=./results
allure serve ./results
python test/test_name.py
python -m unittest tests/test_name.py
pyhton -m unittest test/test_name.py


pytest file.py::Class::test_case

pytest tests/test_name.py -s -v

python -m unittest discover
python -m unittest discover -s tests
python -m unittest discover -s tests -t src
```
### Structure
```
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        |
        ├── fixtures/
        |   ├── test_basic.json
        |   └── test_complex.json
        |
        ├── __init__.py
        └── test_integration.py
```
Or 
`python -m unittest discover -s tests/integration`

### Further information
* https://realpython.com/python-testing/
* https://realpython.com/pytest-python-testing/
* https://realpython.com/python-code-quality/
* https://docs.pytest.org/en/7.1.x/how-to/fixtures.html

