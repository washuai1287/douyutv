from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from douyutv.items import DouyutvItem
from bs4 import BeautifulSoup
from scrapy import Item,Field
import re

class DouyuSpider(Spider):
    name = "douyu"
    start_urls = ["https://www.douyu.com/591967"]
    def parse(self,response):
        items = []
        item = DouyutvItem()
        sel = Selector(response)
        #item['roomId'] = sel.xpath("//a[@class='data-groupdynamic']").extract()
        item['roomId'] = sel.xpath("//script[@type='text/javascript']").re('"room_id":[0-9]*')
        item['name'] = sel.xpath("//a[@class='zb-name']/text()").extract()
        item['title'] = sel.xpath("//h1/text()").extract()
        item['audience'] = sel.xpath("//a[@class='num-v']/text()").extract()
        item['follower'] = sel.xpath("//span[@data-anchor-info='nic']/text()").extract()
        item['weight'] = sel.xpath("//a[@class='weight-v']/text()").extract()
        item['field'] = sel.xpath("//a[contains(@class,'head-room-tag fl')]/text()").extract()
        item['notice'] = sel.xpath("//p[contains(@class,'column-cotent')]/text()").extract()
        item['lastLive'] = sel.xpath("//a[@data-anchor-info='timetit']/text()").extract()
        item['anchorLevel'] = sel.xpath("//a[@class='anchor-level-icon']/@data-anchor-levelimg").extract()
        item['anchorRank'] = sel.xpath("//span[@class='catagory-order-current-order']/span[@class='catagory-order-num-value']/text()").extract
        item['image'] = sel.xpath("//div[@class='anchor-pic fl']/img/@src").extract()
        return item
if __name__ == "__main__":
    sp=DouyuSpider()
    sp.parse()


