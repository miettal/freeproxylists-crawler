import scrapy


class ClarketmProxyListSpider(scrapy.Spider):
    name = 'clarketmproxylist'
    allowed_domains = ['raw.githubusercontent.com']
    start_urls = ['https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt']

    def parse(self, response):
        for line in response.body.decode('utf-8').split('\n'):
            try:
                (ip, port) = line.split(':')
                yield {
                    'ip': ip,
                    'port': port,
                    'protocol': 'http',
                }
            except ValueError:
                pass
