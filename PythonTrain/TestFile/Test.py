from Util.gtfUtil import get_lines

Pa = get_lines('C:/Users/breno/Desktop/intermediateParseA.gtf')
Pb = get_lines('C:/Users/breno/Desktop/intermediateParseB.gtf')
Pc = get_lines('C:/Users/breno/Desktop/intermediateParseC.gtf')
Pd = get_lines('C:/Users/breno/Desktop/intermediateParseD.gtf')

ParseSum = Pa+Pb+Pc+Pd

a = get_lines('C:/Users/breno/Desktop/ParseData/CDS.txt')
b = get_lines('C:/Users/breno/Desktop/ParseData/exon.txt')
c = get_lines('C:/Users/breno/Desktop/ParseData/gene.txt')
d = get_lines('C:/Users/breno/Desktop/ParseData/Selenocysteine.txt')
e = get_lines('C:/Users/breno/Desktop/ParseData/start_codon.txt')
f = get_lines('C:/Users/breno/Desktop/ParseData/five_prime_utr.txt')
g = get_lines('C:/Users/breno/Desktop/ParseData/stop_codon.txt')
h = get_lines('C:/Users/breno/Desktop/ParseData/three_prime_utr.txt')
i = get_lines('C:/Users/breno/Desktop/ParseData/transcript.txt')

sum = a+b+c+d+e+f+g+h+i

if sum == ParseSum:
    print('correto')
else:
    print('erro')
    print(ParseSum)
    print(sum)