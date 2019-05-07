from Util.gtfFindFunctions import gtfFindFunctions


class gtfWriterReferenceClass:

    def __init__(self, filePath):
        self.__originPath = filePath

    # write all features of the file in the other file
    def write_features(self, destination):
        features = gtfFindFunctions.find_features(self.__originPath)
        self.write_feature(features, destination)

    # write all source of the file in the other file
    def write_source(self, destination):
        list = [gtfFindFunctions.find_general_source(self.__originPath), gtfFindFunctions.find_gene_source(self.__originPath), gtfFindFunctions.find_transcript_source(self.__originPath)]
        for x in list:
            self.write_feature(x, destination)

    # write all bio_type of the origin_Path in the other file
    def write_bio_type(self, destination):
        features = gtfFindFunctions.find_bio_type(self.__originPath)
        self.write_feature(features, destination)

    # write all bio_type of the file in the other file
    def write_protein(self, destination):
        features = gtfFindFunctions.find_protein(self.__originPath)
        self.write_feature(features, destination)

    # write all bio_type of the file in the other file
    def write_chromossome(self, destination):
        features = gtfFindFunctions.find_chromossome(self.__originPath)
        self.write_feature(features, destination)

    # method that open the file and really write in the file
    def write_feature(self, features, filePath):
        file = open(filePath, 'a')
        for i in features:
            file.write(i)
            file.write("\n")
        file.close()