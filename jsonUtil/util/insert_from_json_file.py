import json
from DAO.geneDAO import GeneDAO
from collections import Counter

dao = GeneDAO()

# c = Counter()
with open('/home/breno/Downloads/GenomeParser-master/Util/CrawllerObjects/jsonUtil/file.json') as j_file:
    for i in j_file:
        json_lines = json.loads(i)  # return array with dict for each line of the file.json

        gene_nodes = {}

        for json_line in json_lines:
            if gene_nodes.get(json_line.get('GeneID')) is None:
                gene_nodes[json_line.get('GeneID')] = {
                    # 'TranscriptID': [j.get('TranscriptID')],
                    'GeneID': json_line.get('GeneID'),
                    'Genesymbol': json_line.get('Genesymbol'),
                    'SpeciesID': json_line.get('SpeciesID'),
                    'Representativetranscript': json_line.get('Representativetranscript'),
                    'Genedescription': json_line.get('Genedescription'),
                }
        # (1)

    for gene in gene_nodes.values():
        json = {
            "command":
                'INSERT INTO gene CONTENT ' +
                gene.__str__()

        }
        # print(gene.__str__())

        print(dao.save(json))


# (1) Refactor
# else:
#                 y[j.get('GeneID')]['TranscriptID'].append(j.get('TranscriptID'))

# for i in y.values():
#     print(i)
