import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

import random
from fp.fp import FreeProxy
from fp import errors
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

useragent = UserAgent()
chrome_options = webdriver.ChromeOptions()
LINK = 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022'
count = 0
while count <= 89:
    proxy = FreeProxy(rand=True).get()
    # print(proxy)
    chrome_options.add_argument(f'--proxy-server={proxy}')
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"user-agent={useragent.random}")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    browser = driver
    try:

        browser.get(LINK)
        browser.find_element_by_id('inp16').click()
        browser.find_element_by_id('submit_vote').click()
        print(count)
        count += 1
        # time.sleep(8)

    except Exception or errors:
        continue
    finally:
        browser.quit()
        # time.sleep(61)
