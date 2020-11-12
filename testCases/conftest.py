from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser): #This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):# This will return the browser value to the set up method
    return request.config.getoption("--browser")

#### Pytest html report generation####

## Below is the hook for adding Enviornment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] ='NOP Commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']= 'Tester 1'

## Below is the hook for deleting/modify enviornment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
    metadata.pop("Python", None)
    metadata.pop("Platform", None)