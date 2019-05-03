import psycopg2


class Connection:

    @staticmethod
    def get_connection():
        con = psycopg2.connect(host='x', database='cbioportal', user='postgres', password='x')

        return con

    # @staticmethod
    # def get_connection():
    #     con = .o(host='143.107.223.173', database='cbioportal', user='postgres', password='root')
    #
    #     return con
