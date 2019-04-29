import psycopg2


class Connection:

    @staticmethod
    def get_connection():
        con = psycopg2.connect(host='143.107.223.173', database='cbioportal', user='postgres', password='root')

        return con
