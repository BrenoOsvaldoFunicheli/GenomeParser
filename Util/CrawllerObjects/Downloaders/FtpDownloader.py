from CrawllerObjects.AbstractModel.Crawller import Crawler
from CrawllerObjects.CrawlerEngines.ftp_crawler_engine import *
import os


class FtpDownloader(Crawler):

    def __init__(self, **args):
        self.host_dir = args.get('host_dir')
        self.init_dir = args.get('init_dir')
        self.exclude_files = args.get('exclude_files')
        self.conn = ftplib.FTP(args.get('ftp_server_name'))
        self.username = args.get('username')
        self.password = args.get('e-mail')

    def init_connection(self):
        print(self.username, self.password)
        self.conn.login(self.username, self.password)

    def get_files(self):
        self.init_connection()
        # os.chdir(self.host_dir)
        recursive_get(self.conn, self.init_dir)

