import time

from selenium import webdriver

LINK = "http://suninjuly.github.io/registration1.html"
try:

    browser = webdriver.Chrome()
    browser.get(LINK)
    first_name = browser.find_element_by_css_selector('.first_block .first')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector(".first_block .second")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("petrov@mail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
