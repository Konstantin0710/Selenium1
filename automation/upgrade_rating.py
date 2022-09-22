import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from lxml import etree

import random
from fp.fp import FreeProxy
from fp import errors
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from fp.errors import FreeProxyException


xpath = "//div[@class='unicredit_poll_results_block'][5]/span/span[@class='unicredit_poll_results_count']"
useragent = UserAgent()
chrome_options = webdriver.ChromeOptions()
LINK = 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022'
count = 0
while count <= 300:
    try:
        proxy = FreeProxy().get()
        # print(proxy)
        chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument(f"user-agent={useragent.random}")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        browser = driver
        browser.get(LINK)
        browser.find_element_by_id('inp16').click()
        browser.find_element_by_id('submit_vote').click()
        print(f'!!!!!!!!!!!!!!!!!!!!!!!! !{browser.find_element_by_xpath(xpath).text}')
        count += 1
        time.sleep(8)

    except Exception as ex:
        print(ex)
        continue
    finally:
        browser.quit()
        # time.sleep(61)
