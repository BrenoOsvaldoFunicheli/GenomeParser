# from DAO.BioTypeDAO import insert
from DAO.SourceDAO import SourceDAO
from DAO.BioTypeDAO import BioTypeDAO


class InsertController:

    def __init__(self):
        pass

    def insert_bio_type(self, filePath):
        dao = BioTypeDAO()
        var = open(filePath)
        for x in var.readlines():
            dao.insert(x)
        var.close()

    def insert_source(self, filePath):
        dao = SourceDAO()
        var = open(filePath)
        for x in var.readlines():
            dao.insert(x)
        var.close()


