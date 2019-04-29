from Util.gtfFindFunctions import gtfFindFunctions


class GtfWriter:

    def __init__(self, filePath):
        self.__originPath = filePath

    # write all features of the file in the other file
    def write_features(self, destination):
        features = gtfFindFunctions.find_features(self.__originPath)
        self.write_feature(features, destination)

    # write all source of the file in the other file
    def write_source(self, destination):
        features = gtfFindFunctions.find_source(self.__originPath)
        self.write_feature(features, destination)

    # write all gene_source of the file in the other file
    def write_gene_source(self, destination):
        features = gtfFindFunctions.find_gene_source(self.__originPath)
        self.write_feature(features, destination)

    # write all bio_type of the file in the other file
    def write_bio_type(self, destination):
        features = gtfFindFunctions.find_bio_type(self.__originPath)
        self.write_feature(features, destination)

    # method that open the file and really write in the file
    def write_feature(self, features, filePath):
        file = open(filePath, 'a')
        for i in features:
            file.write(i)
            file.write("\n")
        file.close()