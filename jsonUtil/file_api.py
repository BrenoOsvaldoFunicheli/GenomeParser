from requests import *
from DAO.geneDAO import GeneDAO

headers = {"Accept": "application/json"}
x = get('https://rest.genenames.org/search/ensembl_gene_id/', headers=headers)

j = x.json()
x = j['response']['docs']
dao = GeneDAO()

for i in x:
    
    json = {
        "command":
            'INSERT INTO gene CONTENT ' +
            i.__str__()

    }

    print(dao.save(json))
