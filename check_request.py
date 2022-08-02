import requests
from lxml import html
from lxml import etree
from fake_useragent import UserAgent

url_1 = "https://www.nnov.kp.ru"
url_2 = "https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022"
xpath = "//div[@class='unicredit_poll_results_block'][5]/span/span[@class='unicredit_poll_results_count']"
useragent = UserAgent()

payload ='inp-8-0=4&vote=1'
headers = {
    'authority': 'www.nnov.kp.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.nnov.kp.ru',
    'referer': 'https://www.nnov.kp.ru/best/msk/oprosy/nnov_klinikagoda2022',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Mac"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': f'{useragent.random}'
}


cook = requests.request("GET", url_1).cookies
response = requests.request("POST", url_2, data=payload, cookies=cook, headers=headers)
# print(response.text)
tree = etree.HTML(response.text)
tree2 = html.fromstring(response.text)
collection = tree.xpath(xpath)
votes, percentage = collection[0].text.split()
votes = int(votes)

print(votes)