#!/bin/bash

pip install .
python -m freeproxylists_crawler.tools.show_proxies
python -c 'from freeproxylists_crawler.utils import get_proxies; print(get_proxies())'
