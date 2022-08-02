import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

LINK = "http://suninjuly.github.io/selects1.html"





try:

    browser = webdriver.Chrome()
    browser.get(LINK)
    x1 = int(browser.find_element_by_id('num1').text)
    x2 = int(browser.find_element_by_id('num2').text)

    select = Select(browser.find_element_by_tag_name("select"))
    sum1 = x1 + x2
    select.select_by_value(f'{sum1}')  # ищем элемент с текстом "Python"



    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.quit()