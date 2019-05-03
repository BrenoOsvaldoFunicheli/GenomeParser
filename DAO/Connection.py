import psycopg2


class Connection:

    @staticmethod
    def get_connection():
        con = psycopg2.connect(host='x', database='cbioportal', user='postgres', password='x')

        return con
