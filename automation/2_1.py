import math
import time

from selenium import webdriver

LINK = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(LINK)
    x_element = browser.find_element_by_id('treasure')

    x = x_element.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
