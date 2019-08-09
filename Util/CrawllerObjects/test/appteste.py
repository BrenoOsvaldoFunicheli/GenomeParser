from CrawllerObjects.Downloaders.BasicHttpDownloader import BasicHttpDownloader
from CrawllerObjects.PageObjects.PageFilter import PageFilter
from CrawllerObjects.HtmlParsers.LinkParser import LinkParser


p = PageFilter("http://www.targetscan.org/cgi-bin/targetscan/data_download.vert72.cgi")
x = LinkParser()
links = p.filter_page(x)

x = BasicHttpDownloader()
x.get_files(links, '/home/breno/PycharmProjects/untitled/CrawllerObjects/test')

