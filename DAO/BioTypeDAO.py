from DAO.Connection import *


class BioTypeDAO:
    __slots__ = ['con']

    def __init__(self):
        self.con = Connection.get_connection()

    def insert(self, value):
        try:
            cursor = self.con.cursor()
            query = """ INSERT INTO tb_biotype (biotype_name) VALUES (\'"""+value+"""\')"""
            cursor.execute(query, value)

            self.con.commit()

            return cursor.rowcount

        finally:
            # closing database connection.
            if self.con:
                pass
                # cursor.close()
                # con.close()

    def get_all(self):
        try:
            cursor = self.con.cursor()
            query = """ SELECT * FROM tb_biotype"""
            cursor.execute(query)
            result = cursor.fetchall()
        finally:
            # closing database connection.
            cursor.close()
            self.con.close()

        return result