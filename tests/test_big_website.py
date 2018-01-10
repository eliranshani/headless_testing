# coding=utf-8
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("url, title", [
    ("http://www.brandlovescore.com/", "Brand Love Score"),
    ("https://www.hongkiat.com/blog/ui-designer-portfolios/", "20 Beautiful UI & UX Designer Portfolios For Inspiration - Hongkiat"),
    ("https://www.dtelepathy.com/blog/inspiration/14-beautiful-content-heavy-websites-for-inspiration", "14 Beautiful Content-Heavy Websites for Inspiratio"),
    # ("https://www.engadget.com/", "Engadget"),
    ("https://thenextweb.com/", "TNW")
])
def test_check_website_titles(driver, url, title):
    driver.get(url)
    driver.find_element(By.TAG_NAME, "body")
    assert title in driver.title
