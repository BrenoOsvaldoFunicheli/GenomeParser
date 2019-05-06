from DAO.BioTypeDAO import BioTypeDAO
from DAO.ChromossomeDAO import ChromossomeDAO
from DAO.SourceDAO import SourceDAO
from Util.gtfFindFunctions import gtfFindFunctions
from Util.ConvertFlowTable import ConvertFlowTable


class gtfParseByFeature:

    def __init__(self, filePath):
        self.__originPath = filePath

    def parse_gene(self, destination, data=[]):
        # get all the gene that exist on the file
        features = gtfFindFunctions.find_gene(self.__originPath)
        # create the class for connection with database
        chr = ChromossomeDAO().get_all()
        bt = BioTypeDAO().get_all()
        source = SourceDAO().get_all()

        for i in features:
            data.append([i[8],
                         ConvertFlowTable.seq_id_convert(i[0], chr),
                         ConvertFlowTable.bio_type_convert(i[12], bt),
                         ConvertFlowTable.source_convert(i[11], source),
                         i[3],
                         i[4],
                         i[5],
                         i[6],
                         i[9],
                         i[10]])

        self.write_feature(data, destination)

    def parse_gene(self, destination, data=[]):
        # get all the gene that exist on the file
        features = gtfFindFunctions.find_gene(self.__originPath)
        # create the class for connection with database
        chr = ChromossomeDAO().get_all()
        bt = BioTypeDAO().get_all()
        source = SourceDAO().get_all()

        for i in features:
            data.append([i[8],
                         ConvertFlowTable.seq_id_convert(i[0], chr),
                         ConvertFlowTable.bio_type_convert(i[12], bt),
                         ConvertFlowTable.source_convert(i[11], source),
                         i[3],
                         i[4],
                         i[5],
                         i[6],
                         i[9],
                         i[10]])

        self.write_feature(data, destination)

    # write in the file
    def write_feature(self, features, filePath):
        file = open(filePath, 'a')
        # iterate by file and write lines with info about feature
        for i in features:
            length = len(i)
            for j in range(0, length):
                file.write(i[j].__str__())
                file.write('*')
            file.write('\n')
        file.close()

