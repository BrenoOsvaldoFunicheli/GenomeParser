from DAO.DAOUtil import DAOUtil


class GeneDAO(DAOUtil):
    __slots__ = ['con']

    def __init__(self):
        super().__init__()

    def get_all(self):
        query = """SELECT * FROM tb_gene"""
        return super().get_all(query)

    def insert(self, data):
        query = """INSERT INTO tb_gene VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        super().insert(data, query)
