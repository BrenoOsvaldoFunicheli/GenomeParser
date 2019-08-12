import json
from DAO.TranscriptRelationDAO import TranscriptRelationDAO

dao = TranscriptRelationDAO()

with open('/home/breno/Downloads/GenomeParser-master/Util/CrawllerObjects/jsonUtil/file.json') as j_file:
    for i in j_file:
        json_lines = json.loads(i)  # return array with dict for each line of the file.json

        transcript_nodes = {}

        for json_line in json_lines:
            json = {
                "command":
                    "CREATE EDGE transcript_of "
                    "FROM (SELECT FROM transcript WHERE  TranscriptID = '"
                    + json_line.get('TranscriptID') +
                    "') TO (SELECT FROM gene WHERE GeneID = '"
                    + json_line.get('GeneID') +
                    "')"
            }

            print(dao.save(json))
# print(json)
