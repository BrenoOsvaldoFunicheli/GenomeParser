import requests


class Connection:

    def __init__(self, user, password):
        self.session = requests.Session()
        self.session.auth = (user, password)

    def get_connection(self):
        return self.session

