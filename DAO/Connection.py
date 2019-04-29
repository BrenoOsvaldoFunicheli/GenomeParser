import psycopg2


class Connection:

    @staticmethod
    def get_connection():
        con = psycopg2.connect(host='x', database='x', user='postgres', password='root')

        return con
