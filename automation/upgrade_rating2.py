import time

from lxml import html
from lxml import etree
import requests
from fake_useragent import UserAgent
from fp.fp import FreeProxy
import random
from threading import Thread

# headers = {
#     'authority': 'www.nnov.kp.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'ru-RU,ru;q=0.9',
#     'cache-control': 'max-age=0',
#     'content-type': 'application/x-www-form-urlencoded',
#     'cookie': 'uua=6a25c7cc2958477602af71d4bda5442c; _ga_8MQ0FGXD1P=GS1.1.1658428880.1.0.1658428880.0; _ga=GA1.1.434004199.1658428880; _ga=GA1.3.434004199.1658428880; _gid=GA1.3.1258033035.1658428880; _gat_UA-5200037-1=1; _gat_UA-23870775-5=1; _gat_UA-23870775-1=1; _ym_uid=16584288801018608936; _ym_d=1658428880; _ga_BJV4WPQPYC=GS1.1.1658428880.1.0.1658428880.0; _ga_R7DD899R0W=GS1.1.1658428880.1.0.1658428880.0; _ga_R0LEF5ZFCF=GS1.1.1658428880.1.0.1658428880.0; _ym_isad=2; _ym_visorc=b; 265450aab8c9e98c0418f11992199499=1; 979ff45fd0152b8c2947572022b2c317=1; e73acab964c5676461b368aa99e62dd3=1; fbfb3b76297ab4891265a188d4229f0e=1; Cookie_1=value',
#     'origin': 'https://www.nnov.kp.ru',
#     'referer': 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022',
#     'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="102", "Chromium";v="102"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Mac"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': f'{useragent.random}'
# }


url = "https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022"
useragent = UserAgent()
xpath = "//div[@class='unicredit_poll_results_block'][5]/span/span[@class='unicredit_poll_results_count']"


def up_rating(votes):
    proxy = FreeProxy().get()
    vote = 0
    while vote <= votes:
        try:

            proxy_dict = {proxy.split(':')[0]: proxy}
            payload = 'inp-8-0=4&vote=1'
            headers = {
                'authority': 'www.nnov.kp.ru',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'ru-RU,ru;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'uua=6a25c7cc2958477602af71d4bda5442c; _ga_8MQ0FGXD1P=GS1.1.1658428880.1.0.1658428880.0; _ga=GA1.1.434004199.1658428880; _ga=GA1.3.434004199.1658428880; _gid=GA1.3.1258033035.1658428880; _gat_UA-5200037-1=1; _gat_UA-23870775-5=1; _gat_UA-23870775-1=1; _ym_uid=16584288801018608936; _ym_d=1658428880; _ga_BJV4WPQPYC=GS1.1.1658428880.1.0.1658428880.0; _ga_R7DD899R0W=GS1.1.1658428880.1.0.1658428880.0; _ga_R0LEF5ZFCF=GS1.1.1658428880.1.0.1658428880.0; _ym_isad=2; _ym_visorc=b; 265450aab8c9e98c0418f11992199499=1; 979ff45fd0152b8c2947572022b2c317=1; e73acab964c5676461b368aa99e62dd3=1; fbfb3b76297ab4891265a188d4229f0e=1; Cookie_1=value',
                'origin': 'https://www.nnov.kp.ru',
                'referer': 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="102", "Chromium";v="102"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Win"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': f'{useragent.random}'
            }

            response = requests.request("POST", url, headers=headers, data=payload, proxies=proxy_dict)

            tree = etree.HTML(response.text)
            collection = tree.xpath(xpath)
            new_votes, percentage = collection[0].text.split()
            new_votes = int(new_votes)
            print(new_votes)
            if new_votes == vote:
                proxy = FreeProxy(rand=True).get()
            vote = new_votes

        except Exception:
            continue


# up_rating(1624)
for _ in range(10):
    Thread(target=up_rating, args=(task,)).start()