# coding=utf-8
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("url, title", [
    ("http://www.brandlovescore.com/", "Brand Love Score"),
    ("https://www.polygon.com/", "Polygon"),
    ("https://thenextweb.com/", "TNW"),
    ("https://www.blazemeter.com/", "JMeter and Performance Testing for DevOps | BlazeMeter"),
    ("https://www.theverge.com/", "The Verge"),
])
def test_check_website_titles(chrome, firefox, url, title):
    chrome.get(url)
    chrome.find_element(By.TAG_NAME, "body")
    assert title in chrome.title

    firefox.get(url)
    firefox.find_element(By.TAG_NAME, "body")
    assert title in firefox.title








