from gtfparse import read_gtf

#teste de arquivo doc.txt
#abrindo arquivo e escrevendo no arquivo
'''arq = open('C:/Users/breno/Desktop/doc.txt', 'w')
text = 'nome'
#arq = open('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf', 'w')
arq.write(text)
arq.close
'''

#teste falho
'''
count = 0
arq = open('C:/Users/breno/Desktop/doc.txt','r')
#text = arq.read()
#text = arq.readline()
text = arq.readlines()

for line in text:
    print(line)
    ++count
    if count == 2:
        break
arq.close()
'''

arq = open('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf', 'r')
#text = arq.read()
#text = arq.readlines()
#arq.close()

file = open('C:/Users/breno/Desktop/look.gtf','w')
for x in range(100):
    text = arq.readline()
    file.write(text)
    print(text)
    
arq.close()
file.close()

'''
file = open('C:/Users/breno/Desktop/look.gtf', 'r')
text = file.readlines()
for line in text:
    print(line)
'''

''''''
df = read_gtf('C:/Users/breno/Desktop/look.gtf')
df_genes = df[df["feature"] == "gene"]
df_genes_chrY = df_genes[df_genes["seqname"] == "Y"]


parseFile = open('C:/Users/breno/Desktop/parse.txt', 'w')

#print(type(df_genes))
#parseFile.write(str(df_genes))

parseFile.close()

#print(df_genes_chrY)
#parseFile.write(df_genes)
