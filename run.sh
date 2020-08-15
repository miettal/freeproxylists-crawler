#!/bin/bash

pip install .
python -m freeproxylists_crawler.tools.show_proxies
# python -m freeproxylists_crawler.tools.show_proxies --source freeproxylists
# python -m freeproxylists_crawler.tools.show_proxies --source clarketmproxylist
# python -c 'from freeproxylists_crawler.utils import get_proxies; print(get_proxies())'
