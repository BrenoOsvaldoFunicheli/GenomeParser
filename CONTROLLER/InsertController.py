# from DAO.BioTypeDAO import insert
from DAO.SourceDAO import SourceDAO
from DAO.BioTypeDAO import BioTypeDAO
from DAO.ProteinDAO import ProteinDAO
from DAO.ChromossomeDAO import ChromossomeDAO
from DAO.GeneDAO import GeneDAO

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

    def insert_protein(self, filePath):
        dao = ProteinDAO()
        var = open(filePath)
        for x in var.readlines():
            dao.insert(x)
        var.close()

    def insert_chromossome(self, filePath):
        dao = ChromossomeDAO()
        var = open(filePath)
        for x in var.readlines():
            dao.insert(1, x)
        var.close()

    def insert_gene(self, filePath):
        dao = GeneDAO()
        var = open(filePath, 'r')
        for x in var.readlines():
            data = tuple(x.split('*')[0:10])
            dao.insert(data)
        var.close()
