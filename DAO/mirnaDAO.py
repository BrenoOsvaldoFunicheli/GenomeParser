from DAO.DAOUtil import *
from DAO.Connection import *
from DAO.DAOEnum.miRNAEnum import miRNAService
from DAO.DAOEnum.Config import Config


class GeneDAO(DAOUtil):

    def __init__(self):
        super().__init__()
        self.session = ''

    def open(self):
        self.session = Connection(Config.USER, Config.PASSWORD).get_connection()

    def save(self, data):
        self.open()
        return self.session.post(miRNAService.POST(), json=data)

    def update(self, json):
        pass

    def delete(self, json):
        pass

    def __str__(self):
        return 'Session :' + self.session + 'Insert URL:' + self.insert_service
