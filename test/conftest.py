import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options_firefox
from Base.constant import VariabeleAndConst


@pytest.fixture
def create_options_firefox():
    option = options_firefox()
    option.headless = VariabeleAndConst.HEADLESS_BOOLEAN_FIREFOX
    return option

@pytest.fixture
def create_webdriver_firefox(create_options_firefox):
    option = create_options_firefox
    driver = webdriver.Firefox(options=option,
        executable_path=VariabeleAndConst.FIREFOX_GECKODRIVER_PATH)
    return driver

@pytest.fixture(scope='function')
def setup_teardown_driver_firefox(request, create_webdriver_firefox, url=VariabeleAndConst.URL):
    driver = create_webdriver_firefox
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.delete_all_cookies()
    driver.quit()