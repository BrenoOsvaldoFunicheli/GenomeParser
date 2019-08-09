import urllib.request
import CrawllerObjects.CrawlerEngines.ftp_crawler_engine as rf


def basic_download(url_want, local):
    for url in url_want:
        f = urllib.request.urlopen(url)
        print(local + "" + rf.str_trunc(url, split_format='/'))
        data = f.read()
        # print(url)
        with open(local + "" + rf.str_trunc(url, split_format='/'), "wb") as code:
            code.write(data)
            print(url, "concluido")
