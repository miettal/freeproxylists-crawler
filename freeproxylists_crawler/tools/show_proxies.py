import random
import json
from optparse import OptionParser

from scrapy import crawler
from scrapy import signals
from scrapy.signalmanager import dispatcher

from freeproxylists_crawler.spiders.freeproxylists import FreeproxylistsSpider
from freeproxylists_crawler.spiders.clarketmproxylist import ClarketmProxyListSpider


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--source', dest='source', default=None)
    (options, args) = parser.parse_args()

    proxies = []

    def crawler_results(signal, sender, item, response, spider):
        """crawler_results."""
        proxies.append(item)

    if options.source is None:
        spider = random.choice([
            'freeproxylists',
            'clarketmproxylist',
        ])
    elif options.source == 'freeproxylists':
        spider = FreeproxylistsSpider
    elif options.source == 'clarketmproxylist':
        spider = ClarketmProxyListSpider
    else:
        raise Exception

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    crawler_process = crawler.CrawlerProcess({
        'LOG_LEVEL': 'WARNING',
    })
    crawler_process.crawl(spider)
    crawler_process.start()

    for proxy in proxies:
        print(json.dumps(proxy))
