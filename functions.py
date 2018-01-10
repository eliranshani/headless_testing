from selenium.webdriver.common.by import By
import helpers.helpers as utils

url = "http://blazedemo.com"


def submit_form(driver):
    driver.find_element(By.XPATH, "//input[@type='submit']").click()


def find_flight_in_dropdown(dropdown_element, expected_flight):
    for option in dropdown_element.find_elements_by_tag_name('option'):
        if option.text == expected_flight:
            option.click()


def choose_departure_flight(driver, departure_flight):
    from_port_dropdown = utils.find_element(driver, By.NAME, "fromPort")
    find_flight_in_dropdown(dropdown_element=from_port_dropdown, expected_flight=departure_flight)


def choose_arrival_flight(driver, arrival_flight):
    to_port_dropdown = utils.find_element(driver, By.NAME, "toPort")
    find_flight_in_dropdown(dropdown_element=to_port_dropdown, expected_flight=arrival_flight)