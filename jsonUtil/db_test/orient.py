import json, requests
import abc
from DAO.geneDAO import GeneDAO

#
#
# x = requests.post("http://143.107.223.238:2480/class/mirna_path/gene")
# session = requests.Session()
# session.auth = ('root', 'rtpwd')
# # result = session.get("http://localhost:2480/class/mirna_path/gene")
#
# x = session.post('http://143.107.223.238:2480/command/mirna_path/sql',
#                  json={
#                      "command":
#                          'INSERT INTO gene CONTENT '
#                          '{"name": "PTEN1", "surname": "G"}'
#                  })

# print(x.content)
x = GeneDAO()
# print(x)
# #
json = {
    "command":
        'INSERT INTO gene CONTENT '
        '{"name": "PTEN1", "surname": "G"}'
}
#
#
print(x.save(json))
# x = session.post('http://localhost:2480/document/mirna_path',
#                  json={
#                      "@class": "gene",
#                      "name": "BRCA1",
#                  }
#                  )
#
# print(x.content)

# #
