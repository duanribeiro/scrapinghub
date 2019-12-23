# -*- coding: utf-8 -*-
import scrapy
# Any additional imports (items, libraries,..)


class TrialSpider(scrapy.Spider):
    name = 'trial'
    start_urls = [
        'http://pstrial-a-2018-10-19.toscrape.com/browse/'
    ]  # put your start urls here

    def parse(self, response):
        # Put your logic to process artworks directory

        final_object = {
            "url": "",
            "artist": [""],
            "title": "",
            "image": "",
            "height": 0,
            "width":  0,
            "description": "",
            "categories": [""],
        }
        pass