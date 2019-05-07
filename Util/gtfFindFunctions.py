from gtfparse import read_gtf


class gtfFindFunctions:

    @staticmethod
    def find_features(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        feature = df["feature"].__array__()
        return set(feature)

    @staticmethod
    def find_general_source(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df["source"].__array__()
        return set(source_array)

    @staticmethod
    def find_gene_source(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df["gene_source"].__array__()
        return set(source_array)

    @staticmethod
    def find_transcript_source(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df["transcript_source"].__array__()
        return set(source_array)

    @staticmethod
    def find_bio_type(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df["gene_biotype"].__array__()
        return set(source_array)

    @staticmethod
    def find_chromossome(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df["seqname"].__array__()
        return set(source_array)

    @staticmethod
    def find_gene(filePath):
        # open the file
        df = read_gtf(filePath)
        # filter of info based in the columns
        # translate a DateFrame in array for manipulation
        source_array = df[df["feature"] == 'gene'].__array__()
        return source_array
