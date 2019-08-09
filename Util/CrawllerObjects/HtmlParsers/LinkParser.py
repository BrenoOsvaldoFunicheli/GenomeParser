from html.parser import HTMLParser
from urllib.request import urlopen
from CrawllerObjects.CrawlerEngines.ftp_crawler_engine import str_trunc


class LinkParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        """

        :param tag: They are param of the html page that will be pass by filter of the class HTMLParser
        :param attrs:
        :return:
        """
        if tag == 'a':

            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

    def filter(self, exts=['.zip', '.txt', '.xls']):
        """
        # x = [link for ext in exts if plink[len(ext):] == ext]

        :param exts: This param show exts that will be filtered by method, for example .zip, .csv
        :return:
        """
        parsed_link = []
        for link in self.links:
            plink = str_trunc(link, split_format='/')

            for ext in exts:
                elen = len(ext)
                if plink[-elen:] == ext:
                    parsed_link.append(link)
                    break

        return parsed_link
