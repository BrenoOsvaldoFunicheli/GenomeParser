from DAO.Connection import *


class ProteinDAO:
    __slots__ = ['con']

    def __init__(self):
        self.con = Connection.get_connection()

    def insert(self, value):
        try:
            cursor = self.con.cursor()
            query = """ INSERT INTO tb_biotype (protein_name) VALUES (\'"""+value+"""\')"""
            cursor.execute(query, value)

            self.con.commit()

            return cursor.rowcount

        finally:
            # closing database connection.
            if self.con:
                pass
                # cursor.close()
                # con.close()

