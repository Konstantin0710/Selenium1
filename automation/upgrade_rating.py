import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
useragent = UserAgent()
chrome_options = webdriver.ChromeOptions()
import random


LINK = 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022'

for _ in range(10):

    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"user-agent={useragent.random}")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    browser = driver
    try:

        browser.get(LINK)
        browser.find_element_by_id('inp16').click()
        time.sleep(5)
        browser.find_element_by_id('submit_vote').click()
    finally:
        time.sleep(10)
        browser.quit()
