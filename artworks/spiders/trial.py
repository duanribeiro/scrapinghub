# -*- coding: utf-8 -*-
import scrapy
from artworks.items import ArtworksItem

from scrapy.utils.response import open_in_browser

# Any additional imports (items, libraries,..)


class TrialSpider(scrapy.Spider):
    name = 'trial'

    def start_requests(self):
        url = "http://pstrial-a-2018-10-19.toscrape.com/browse/"

        yield scrapy.http.FormRequest(url=url,
                                      method='GET',
                                      callback=self.parse_browse)

    def parse_browse(self, response):
        # First, lets check the summertime <div> and his subsections
        summertime_div = response.xpath('//*[@id="subcats"]/div[5]')
        for item in summertime_div.css('li'):
            url_summertime_subitens = response.urljoin(item.css('a').attrib['href'])

            yield scrapy.http.FormRequest(url=url_summertime_subitens,
                                          method='GET',
                                          callback=self.parse_final,
                                          meta={'categorie': url_summertime_subitens.split('/')[-1]})

        # Then, lets check the in sunsh <a> link
        in_sunsh_a = response.xpath('//*[@id="subcats"]/div[3]/a')
        if in_sunsh_a.attrib['href']:
            url_in_sunsh = response.urljoin(in_sunsh_a.attrib['href'])

            yield scrapy.http.FormRequest(url=url_in_sunsh,
                                          method='GET',
                                          callback=self.parse_final,
                                          meta={'categorie':'in_sunsh'})

    def parse_final(self, response):
        return_object = ArtworksItem()
        list_artist = []

        for item in response.xpath('//*[@id="body"]/div[2]').css('a'):
            if 'Artist' in item.css('div').css('h2').get():
                for artist in item.css('div').css('h2').get().split('Artist: ')[1:]:
                    list_artist.append(artist.split('<')[0].split(';')[0])

            return_object = {
                "url": item.css('a').attrib['href'],
                "artist": list_artist,
                "title": item.css('h1').get().split('>')[1].split('<')[0],
                "image": item.css('img').attrib['src'],
                "height": 0,
                "width":  0,
                "description": "",
                "categories": [response.meta['categorie']],
            }

            yield return_object
