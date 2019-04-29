from gtfparse import read_gtf


#
# var = get_features()
# for feature in var:
#     # file_Path = 'C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf'
# file_Path = 'C:/Users/breno/Desktop/intermediateParseA.gtf'
#     destination = 'C:/Users/breno/Desktop/'+feature+'.txt'
#     letter = ['A.gtf', 'B.gtf', 'C.gtf', 'D.gtf']
#     for i in letter:
#         breno_parseGTF(file_Path + i, feature, destination)

# var = open('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf')
#
# for i in range(0, 5):
#     print(var.readline())
#
# # GTF_to_text_wtih_percent(file_Path, 0.05)
#
# var = 'C:/Users/breno/Desktop/min.gtf'
#
# f = find_source(var)
# # var = open(file_Path, 'w')
# #
# df = read_gtf(var)
# # df_exon = df[df["feature"] == 'transcript']
# df_exon = df[df["feature"] == 'exon']
# df_CDS = df[df["feature"] == 'CDS']
# df_gene = df[df["feature"] == 'gene']
# var = df_gene.__array__()
# ver = df_exon.__array__()
# vdr = df_CDS.__array__()
# print(var[0])
#
# for i in range(0, 1):
#     print(ver[i])
#     print(vdr[i])
#
# # print(var[1])
# # print(var[12])
# #
# # df_gene = df[df['feature'] == 'gene']
# #
# # ar = df_gene.__array__()
#

from Util.gtfWriter import GtfWriter
#
gt = GtfWriter('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf')
gt.write_protein('C:/Users/breno/Desktop/protein.txt')

# from CONTROLLER.InsertController import InsertController
#
# insertion = InsertController()
#
# insertion.insert_source('C:/Users/breno/Desktop/source.txt')