from urllib.request import *
from CrawllerObjects.HtmlParsers.LinkParser import LinkParser

class PageFilter:

    def __init__(self, url):
        self.infile = urlopen(url)

    def open_file(self):
        return self.infile.read()

    def close_file(self):
        return self.infile.close()

    def format_file(self):
        """

        :rtype: object
        """
        html = self.open_file()
        html_string = html.decode()
        self.close_file()
        return html_string

    def filter_page(self, parser):
        """

        :type parser: object
        """
        str_html = self.format_file()
        x = LinkParser()
        x.feed(str_html)
        return x.filter()
