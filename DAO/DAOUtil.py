from DAO.Connection import *


class DAOUtil:
    __slots__ = ['con']

    def __init__(self):
        self.con = Connection.get_connection()

    # code that do insert into database in table seq_name
    def insert(self, data, query):
        try:
            cursor = self.con.cursor()
            cursor.execute(query, data)
            self.con.commit()
            return cursor.rowcount

        finally:
            if self.con:
                pass

    def get_all(self, query):
        try:
            cursor = self.con.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

        finally:
            # closing database connection.
            cursor.close()
            self.con.close()

        return result
