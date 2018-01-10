import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (e.g. chrome)")
    parser.addoption("--headless", action="store", default="headless", help="Is headless driver?")


@pytest.yield_fixture(scope="function", autouse=True)
def driver(request):

    browser = request.config.getoption("--driver")

    if browser != 'chrome':
        pytest.fail('only chrome is supported at the moment')
        return

    headless = request.config.getoption("--headless")
    chrome_options = webdriver.ChromeOptions()
    if headless == "true":
        # Set headless flag to true
        chrome_options.add_argument("headless")

    # Initiate Chrome
    browser = webdriver.Chrome(chrome_options=chrome_options)

    yield browser

    browser.quit()
