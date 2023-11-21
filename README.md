# Pytest Framework Guide

**This instruction requires local admin permissions in order to be able to install all needed components.**

## Setup

Install Python, PyCharm and needed libraries

* [Python](https://www.python.org/downloads/) - (at least 3.10+ version) please remember to add Python to PATH during
  installation by selecting appropriate checkbox.
* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) - please download Community Edition and after
  installation choose “Virtual Environment” as environment type when you open a project for the first time.
* [Allure framework](https://allurereport.org/docs/) - please download allure-framework and install it. As for manual
  installation we can find infromation [here](https://allurereport.org/docs/gettingstarted-installation/)
* Install pytest Framework and dependencies from ```requirements.txt``` file by
  typing ```pip install -r requirements.txt``` from PyCharm terminal level.

## Running Pytest Framework tests
Run pytest command for example:  ```pytest --alluredir=report/report_raw```

It is important to know that all file paths (both for resource files and test data) are relative to place from which
test was invoked. Entire solution is prepared for test invocation from main catalogue.

## Pytest command arguments examples

```pytest -n 5 tests/01_basic_function_for_luma_test.py --allure-severities blocker,critical --alluredir=report/report_raw --capture_screenshots=True```

* ```-n 5``` - Allows to run tests in parallel mode using 5 processes
* ```--alluredir=report/report_raw``` - Specifies to which raw files folder results will be stored (json files,
  screenshots etc.)
* ```pytest tests/01_login_test.py``` - Runs specific test file in project, without file pytest will run every test in
  project
* ```--allure-severities normal,critical``` - Runs all tests with specific severity, we can also
  use ```--allure-epics```,
  ```--allure-features```
* ```--capture_screenshots=True``` - Changes ALLOW_SCREENSHOT flag from resources.variables.py file
  (by default it is set as False). When flag is "True", screenshots with red rectangle around found element will
  be attached to allure report (it can be used as documentation or instruction how to do some operations).

## Allure report generation

After running tests we will have raw files which will be used in generation of allure report. To generate html version
of report we need to use command:
```allure generate report/report_raw -o report/report_html --clean```

* ```report/report_raw``` - Specifies where we have raw files to generate report
* ```-o report/report_html``` - Specifies where generated html report will be stored
* ```--clean``` - Cleans report destination folder which is leading to clear run history

Also we can use `.bat` file to generate report:

```report/generate_new_report.bat```

## Allure report browse

To see html version of allure report we can use `.bat` file which starts local server.

```report/run_allure_server.bat``` 

We can also use command which will open server on port 9999

```allure open report/report_html --port 9999``` 

## Naming conventions

Located in tests folder test suite files contain test cases to be run by the tool. File names must contain "test"
in start or end of file name for example: ```01_login_test.py```

Naming convention for the files is the same as written
in [Pep 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

