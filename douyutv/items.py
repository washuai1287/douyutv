# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item,Field

class DouyutvItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    roomId = Field()
    name = Field()
    title = Field()
    follower = Field()
    audience = Field()
    weight = Field()
    field = Field()
    notice = Field()
    lastLive = Field()
    anchorLevel = Field()
    anchorRank = Field()
    image = Field()
    pass
