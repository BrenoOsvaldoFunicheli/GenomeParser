class ConvertFlowTable:

    # return the id of the seqname based in value string
    @staticmethod
    def seq_id_convert(value, result):
        for x in result:
            if x[2].strip() == value:
                return x[0]
        return ''

    @staticmethod
    def bio_type_convert(value, result):
        for x in result:
            if x[1].strip() == value:
                return x[0]
        return ''

    @staticmethod
    def source_convert(value, result):
        for x in result:
            if x[1].strip() == value:
                return x[0]
        return ''