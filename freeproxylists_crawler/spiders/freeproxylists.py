# -*- coding: utf-8 -*-
import re
import urllib.parse

import scrapy


class FreeproxylistsSpider(scrapy.Spider):
    name = 'freeproxylists'
    allowed_domains = ['www.freeproxylists.net']
    start_urls = ['http://www.freeproxylists.net/']

    def parse(self, response):
        tbl = response.css('table')[1]
        for tr in tbl.css('tr'):
            try:
                ip = urllib.parse.unquote(tr.css('td script::text').re('IPDecode\\("(.+)"\\)')[0])
                ip = re.match('<a href=".+">(.+)</a>', ip).group(1)
                port = int(tr.css('td::text').extract()[0])
                protocol = 'http' if tr.css('td::text').extract()[1] == 'HTTP' else 'https'
                rate = float(tr.css('td::text').extract()[6][:-1]) / 100.0
                yield {
                    'ip': ip,
                    'port': port,
                    'protocol': protocol,
                    'rate': rate,
                }
            except IndexError:
                pass

        for href in response.css('.page a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href))
