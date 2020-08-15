from setuptools import find_packages
from setuptools import setup


setup(
    name='freeproxylists-crawler',
    packages=find_packages(),
    install_requires=[
        'Scrapy',
        'scrapy-selenium @ git+https://github.com/clemfromspace/scrapy-selenium.git@develop',
    ],
)
