from gtfparse import *


class ParseData:

    def parse_cds(self, filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        str_cds = df[df["feature"] == 'CDS'].__array__()
        print(str_cds)