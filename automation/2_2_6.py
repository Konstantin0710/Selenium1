import math
import time

from selenium import webdriver

LINK = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(LINK)
    x_element = browser.find_element_by_id('input_value')
    y = calc(x_element.text)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    option1 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()