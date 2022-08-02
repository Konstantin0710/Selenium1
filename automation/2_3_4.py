import time
from selenium import webdriver
import math

LINK = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    browser.find_element_by_css_selector('.btn').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    browser.find_element_by_css_selector('.btn').click()



finally:
    time.sleep(10)
    browser.quit()
