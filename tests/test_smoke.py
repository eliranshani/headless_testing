import pytest
from selenium.webdriver.common.by import By
import helpers.helpers as utils

url = "http://blazedemo.com"


def submit_form(chrome):
    chrome.find_element(By.XPATH, "//input[@type='submit']").click()


def find_flight_in_dropdown(dropdown_element, expected_flight):
    for option in dropdown_element.find_elements_by_tag_name('option'):
        if option.text == expected_flight:
            option.click()


def choose_departure_flight(chrome, departure_flight):
    from_port_dropdown = utils.find_element(chrome, By.NAME, "fromPort")
    find_flight_in_dropdown(dropdown_element=from_port_dropdown, expected_flight=departure_flight)


def choose_arrival_flight(chrome, arrival_flight):
    to_port_dropdown = utils.find_element(chrome, By.NAME, "toPort")
    find_flight_in_dropdown(dropdown_element=to_port_dropdown, expected_flight=arrival_flight)


@pytest.fixture(scope="function")
def open_website(chrome):
    chrome.get(url)
    chrome.find_element(By.TAG_NAME, "form")
    assert chrome.title == "BlazeDemo"


@pytest.mark.parametrize('from_port, to_port', [
    ("Paris", "Buenos Aires"),
    ("Philadelphia", "Rome"),
    ("Boston", "London"),
    ("Portland", "Berlin"),
    ("San Diego", "New York"),
    ("Mexico City", "Dublin"),
])
def test_find_flights(chrome, open_website, from_port, to_port):

    # Find flight
    choose_departure_flight(chrome, departure_flight=from_port)
    choose_arrival_flight(chrome, arrival_flight=to_port)
    submit_form(chrome)

    assert from_port in utils.get_text(chrome, By.TAG_NAME, "h3")
    assert to_port in utils.get_text(chrome, By.TAG_NAME, "h3")
    assert "reserve.php" in chrome.current_url

    # Choose flight
    submit_form(chrome)

    assert from_port in utils.get_text(chrome, By.TAG_NAME, "h2")
    assert to_port in utils.get_text(chrome, By.TAG_NAME, "h2")
    assert "purchase.php" in chrome.current_url

    # Purchase flight
    submit_form(chrome)

    assert "Thank you for your purchase today!" in utils.get_text(chrome, By.TAG_NAME, "h1")
    assert "confirmation.php" in chrome.current_url


def test_teardown(chrome):
    chrome.quit()
