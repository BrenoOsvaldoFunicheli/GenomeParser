from DAO.Connection import *


class ChromossomeDAO:
    __slots__ = ['con']

    def __init__(self):
        self.con = Connection.get_connection()

    # code that do insert into database in table seq_name
    def insert(self, id_genome, seqname):
        try:
            cursor = self.con.cursor()
            query = """ INSERT INTO tb_seq_names (id_genome, seqname) VALUES (%s,%s)"""
            data = (id_genome, seqname)

            cursor.execute(query, data)

            self.con.commit()

            return cursor.rowcount

        finally:

            if self.con:
                pass

    def get_all(self):
        try:
            cursor = self.con.cursor()
            query = """ SELECT * FROM tb_seq_names"""
            cursor.execute(query)
            result = cursor.fetchall()

        finally:
            # closing database connection.
            cursor.close()
            self.con.close()

        return result
