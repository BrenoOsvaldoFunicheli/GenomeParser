import abc


class Crawler(abc.ABC):

    @abc.abstractmethod
    def get_files(self):
        pass
