from CrawllerObjects.DAO.DAOUtil import *
from CrawllerObjects.DAO.Connection import *


class GeneDAO(DAOUtil):

    def __init__(self, url):
        super().__init__(url)
        self.insert_url = url
        self.session = ''

    def open(self):
        self.session = Connection('root', 'rtpwd').get_connection()

    def save(self, json):
        self.open()
        print(json)
        print(self.insert_url)
        x = self.session.post(self.insert_url, json)
        print(x.content)

    def update(self, json):
        pass

    def delete(self, json):
        pass
