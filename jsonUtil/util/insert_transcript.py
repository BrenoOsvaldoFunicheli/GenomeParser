import json
from DAO.TranscriptRelationDAO import TranscriptRelationDAO

dao = TranscriptRelationDAO()

with open('/home/breno/Downloads/GenomeParser-master/Util/CrawllerObjects/jsonUtil/file.json') as j_file:
    for i in j_file:
        json_lines = json.loads(i)  # return array with dict for each line of the file.json

        transcript_nodes = {}

        for json_line in json_lines:
            if transcript_nodes.get(json_line.get('TranscriptID')) is None:
                transcript_nodes[json_line.get('TranscriptID')] = {
                    'TranscriptID': json_line.get('TranscriptID')
                }

    for transcript in transcript_nodes.values():
        json = {
            "command":
                'INSERT INTO transcript CONTENT ' +
                transcript.__str__()
        }

        # print(json)
        print(dao.save(json))
