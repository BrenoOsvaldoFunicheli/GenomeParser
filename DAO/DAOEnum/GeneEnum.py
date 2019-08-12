from DAO.DAOEnum.Config import Config


class GeneService:
    _GET = ''
    _POST = "/command/mirna_path/sql"
    _DELETE = ''

    @staticmethod
    def POST():
        """

        :return: adress rest server join with POST service
        """
        return Config.SERVER + GeneService._POST
