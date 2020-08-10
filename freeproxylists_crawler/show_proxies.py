import json
from optparse import OptionParser

from scrapy import crawler
from scrapy import signals
from scrapy.signalmanager import dispatcher

from freeproxylists_crawler.spiders.freeproxylists import FreeproxylistsSpider


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--minimum-rate', dest='minimum_rate')
    parser.add_option('--protocol', dest='protocol')
    (options, args) = parser.parse_args()

    proxies = []

    def crawler_results(signal, sender, item, response, spider):
        """crawler_results."""
        proxies.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    crawler_process = crawler.CrawlerProcess({
        'LOG_LEVEL': 'WARNING',
    })
    crawler_process.crawl(FreeproxylistsSpider)
    crawler_process.start()

    for proxy in proxies:
        if options.minimum_rate is not None and proxy['rate'] < options.minimum_rate:
            continue
        if options.protocol is not None and options.protocol != proxy['protocol']:
            continue
        print(json.dumps(proxy))
