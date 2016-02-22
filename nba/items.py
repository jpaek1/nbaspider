# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NBATeam(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    teamname = scrapy.Field()
    roster = scrapy.Field()
    num_members = scrapy.Field()
    ppg_leaders = scrapy.Field()
    reb_leaders = scrapy.Field()
    ast_leaders = scrapy.Field()
    stl_leaders = scrapy.Field()
    blk_leaders = scrapy.Field()

class Player(scrapy.Item):
    name = scrapy.Field()
    gp = scrapy.Field()
    mins = scrapy.Field()
    fgm = scrapy.Field()
    fga = scrapy.Field()
    fgp = scrapy.Field()
    threepm = scrapy.Field()
    threepa = scrapy.Field()
    threepp = scrapy.Field()
    ftm = scrapy.Field()
    fta = scrapy.Field()
    ftp = scrapy.Field()
    oreb = scrapy.Field()
    dreb = scrapy.Field()
    reb = scrapy.Field()
    ast = scrapy.Field()
    to = scrapy.Field()
    stl = scrapy.Field()
    blk = scrapy.Field()
    pf = scrapy.Field()
    ppg = scrapy.Field()
