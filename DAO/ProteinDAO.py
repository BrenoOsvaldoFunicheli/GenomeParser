from DAO.DAOUtil import DAOUtil


class ProteinDAO(DAOUtil):
    __slots__ = ['con']

    def __init__(self):
        super().__init__()

    def get_all(self):
        query = """SELECT * FROM tb_protein"""
        return super().get_all(query)

    def insert(self, data):
        query = """INSERT INTO tb_biotype (protein_name) VALUES (%s)"""
        super().insert(data, query)
