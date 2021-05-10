from selenium import webdriver
#import time


def test_guest_should_see_cart_button(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(30)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(button) != 0, "The button is missing"

