from CrawllerObjects.AbstractModel.Crawller import Crawler
from CrawllerObjects.CrawlerEngines.http_crawler_engine import *


class BasicHttpDownloader(Crawler):

    def __init__(self):
        self._want_files = []

    @property
    def want_files(self):
        return self._want_files

    @want_files.setter
    def want_files(self, lvalue):
        self._want_files = lvalue

    def get_files(self, urls, local):
        self._want_files = urls
        basic_download(self._want_files, local)
