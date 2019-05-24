import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from bilibili1.items import BilibiliItem
class MySpider(scrapy.Spider):
    name = "mySpider"
    #key = "python"
    #source_url = "https://www.bilibili.com/ranking/all/0/0/3"


    def start_requests(self):
        #url = MySpider.source_url+"search?utf8=%E2%9C%93&q="+MySpider.key
        url = "https://www.bilibili.com/ranking/all/0/0/3"
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        try:
            dammit = UnicodeDammit(response.body,["utf-8","gbk"])
            data =dammit.unicode_markup
            selector = scrapy.Selector(text=data)
            lis = selector.xpath("//li[@class='rank-item']")
            for li in lis:
                title = li.xpath("./div/div/a/text()").extract_first()
                num = li.xpath("./div/div/div/span[position()=1]/text()").extract_first()
                top = li.xpath("./div/text()").extract_first()
                author = li.xpath("./div/div/div/a/span/text()").extract_first()
                comment_num = li.xpath("./div/div/div/span[position()=2]/text()").extract_first()
                item = BilibiliItem()
                item["title"]=title.strip() if title else ""
                item["num"] = num.strip() if num else ""
                item["top"] = top.strip() if top else ""
                item["author"] = author.strip() if author else ""
                item["comment_num"] = comment_num.strip() if comment_num else ""
                yield item

        except Exception as err:
            print(err)