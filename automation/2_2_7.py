import os
import time
from selenium import webdriver

LINK = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    first_name = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    first_name.send_keys("Ivan")
    second_name = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    second_name.send_keys("Ivanov")
    email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    email.send_keys('iii@kas.com')
    file = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(8)
    browser.quit()
