from gtfparse import read_gtf, parse_gtf_and_expand_attributes
# returns GTF with essential columns such as "feature", "seqname", "start", "end"
# alongside the names of any optional keys which appeared in the attribute column
def GTF_to_text_wtih_percent(path, percent):

    source = open(path, 'r')
    min_size = open('C:/Users/breno/Desktop/min.gtf', 'w')

    if percent < 1:
        file_size = int(get_lines(path) * percent)
        for i in range(file_size):
            text = source.readline()
            min_size.write(text)
    else:
        print('o valor tem que ser uma percentagem menor que 1')

    min_size.close()
    source.close()

def GTF_to_text(path):

    source = open(path, 'r')
    intermediateA = open('C:/Users/breno/Desktop/intermediateParseA.gtf', 'w')
    intermediateB = open('C:/Users/breno/Desktop/intermediateParseB.gtf', 'w')
    intermediateC = open('C:/Users/breno/Desktop/intermediateParseC.gtf', 'w')
    intermediateD = open('C:/Users/breno/Desktop/intermediateParseD.gtf', 'w')

    # get the total line numbers
    # divide lines in 4 before
    file_size = get_lines(path)
    sizeA = file_size // 4
    sizeB = sizeA * 2
    sizeC = sizeA * 3
    sizeD = sizeA * 4

    # iterates through several lines by
    # taking each line of the file and
    # writing in the other files
    # write in 4 files different oriented by number lines
    for x in range(file_size):
        text = source.readline()
        if x < sizeA:
            intermediateA.write(text)
        elif (x >= sizeA) and (x < sizeB):
            intermediateB.write(text)
        elif (x >= sizeB) and (x < sizeC):
            intermediateC.write(text)
        else:
            intermediateD.write(text)

    # close the files
    source.close()
    intermediateA.close()
    intermediateB.close()
    intermediateC.close()
    intermediateD.close()

def breno_parseGTF(FilePath, Feature, FileDestination):
    # open the file
    df = read_gtf(FilePath)
    # filter of info based in the columns
    # translate a DateFrame in array for manipulation
    str_genes = df[df["feature"] == Feature].__array__()
    # get quantity of the genes and storage in the variable tam
    tam = len(str_genes)
    # open the file for write
    files_gene = open(FileDestination, 'a')
    # iterate by array and write in the file
    for j in range(0, tam - 1):
        for k in range(0, 25):
            # write the feature one an one
            # before insert a space bar for count the number de attr
            files_gene.write('|')
            files_gene.write(str_genes[j][k].__str__())
            files_gene.write('|')
        # jump line in the file before write a position of the array
        files_gene.write('\n')
    files_gene.close()

# get total of lines
def get_lines (file_name):

    # open the file
    file = open(file_name, "r")
    # sum the total iterating by line of the files
    n_line = sum(1 for line in file)
    file.close()
    return n_line

def get_features():
    feature_file = open('C:/Users/breno/Desktop/feturetypes.txt', 'r')
    f = []
    for feature in feature_file:
        f.append(feature)
    feature_file.close()
    result = f[0].split(" ")
    return result

