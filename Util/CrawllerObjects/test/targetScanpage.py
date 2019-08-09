from collections import Counter

mirna_info = {}
tcga_data = {}

# rsp = input('qual micro ?')

with open('/home/breno/PycharmProjects/untitled/mirbase_parser/CURRENT/database_files/mirna.txt', 'r') as p:
    for i in p:
        mirna_info[i.split('\t')[2]] = i.split('\t')

for i in mirna_info:
    print(i)

with open(
        '/home/breno/PycharmProjects/untitled/CrawllerObjects/test/pancanMiRs_EBadjOnProtocolPlatformWithoutRepsWithUnCorrectMiRs_08_04_16.xena',
        'r') as p:
    x = 0
    for i in p:
        tcga_data[i.split('\t')[0]] = i.split()

# print(tcga_data)
for i in tcga_data.values():
    # pass
    # print(i)
    if len(i) > 3:
        if mirna_info.get(i[0]) != None:
            print(mirna_info.get(i[0]))
# break
# x = Counter(y)
# print(tcga_data)
# for i in mirna_info.items():
# print(i)
