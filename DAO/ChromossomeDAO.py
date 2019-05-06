from DAO.DAOUtil import DAOUtil


class ChromossomeDAO(DAOUtil):
    __slots__ = ['con']

    def __init__(self):
        super().__init__()

    def get_all(self):
        query = """SELECT * FROM tb_seq_names"""
        return super().get_all(query)

    def insert(self, data):
        query = """INSERT INTO tb_seq_names (id_genome, seqname) VALUES (%s,%s)"""
        super().insert(data, query)
