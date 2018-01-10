import pytest
from selenium.webdriver.common.by import By
import helpers.helpers as utils
import functions as func


@pytest.fixture(scope="function")
def open_website(driver):
    driver.get(func.url)
    driver.find_element(By.TAG_NAME, "form")
    assert driver.title == "BlazeDemo"


@pytest.mark.parametrize('from_port, to_port', [
    ("Paris", "Buenos Aires"),
    ("Philadelphia", "Rome"),
    ("Boston", "London"),
    ("Portland", "Berlin"),
    ("San Diego", "New York"),
    ("Mexico City", "Dublin"),
])
def test_find_flights(driver, open_website, from_port, to_port):

    # Find flight
    func.choose_departure_flight(driver, departure_flight=from_port)
    func.choose_arrival_flight(driver, arrival_flight=to_port)
    func.submit_form(driver)

    assert from_port in utils.get_text(driver, By.TAG_NAME, "h3")
    assert to_port in utils.get_text(driver, By.TAG_NAME, "h3")
    assert "reserve.php" in driver.current_url

    # Choose flight
    func.submit_form(driver)

    assert from_port in utils.get_text(driver, By.TAG_NAME, "h2")
    assert to_port in utils.get_text(driver, By.TAG_NAME, "h2")
    assert "purchase.php" in driver.current_url

    # Purchase flight
    func.submit_form(driver)

    assert "Thank you for your purchase today!" in utils.get_text(driver, By.TAG_NAME, "h1")
    assert "confirmation.php" in driver.current_url


def test_teardown(driver):
    driver.close()
    driver.quit()
