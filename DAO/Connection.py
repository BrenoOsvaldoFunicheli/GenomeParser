import requests


class Connection:

    def __init__(self, user, password):
        self.session = requests.Session()
        self.session.auth = (user, password)

    def get_connection(self):
        """

        :return: Session object with authentication of user and password
        """
        return self.session

