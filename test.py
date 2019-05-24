import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from bilibili1.items import BilibiliItem
import requests
from requests.exceptions import RequestException



name = "mySpider"
key = "python"
url = "https://www.bilibili.com/ranking/all/0/0/3"



def get_one_page(url):
    # headers, 伪装成浏览器
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (HTML, like Gecko) '
                    'Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
html = get_one_page(url)
selector = scrapy.Selector(text=html)
lis = selector.xpath("//li[@class='rank-item']")
for li in lis:
    title = li.xpath("./div/div/div/span[position()=2]/text()").extract_first()
    print(title)
    #print(li.extract())
print(lis)
