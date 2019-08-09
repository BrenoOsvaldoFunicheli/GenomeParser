import abc


class DAOUtil(abc.ABC):

    def __init__(self, url):
        super().__init__()
        self.url = url

    @staticmethod
    def save(self, json):
        pass

    @staticmethod
    def update(self, json):
        pass

    @staticmethod
    def delete(self, json):
        pass

