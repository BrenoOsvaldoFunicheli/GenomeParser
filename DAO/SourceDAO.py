from DAO.DAOUtil import DAOUtil


class SourceDAO(DAOUtil):
    __slots__ = ['con']

    def __init__(self):
        super().__init__()

    def get_all(self):
        query = """ SELECT * FROM tb_source"""
        return super().get_all(query)

    def insert(self, data):
        query = """INSERT INTO tb_source (source_name) VALUES ($s)"""
        super().insert(data, query)
