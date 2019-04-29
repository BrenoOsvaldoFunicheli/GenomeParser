from gtfparse import read_gtf, parse_gtf_and_expand_attributes


# returns GTF with essential columns such as "feature", "seqname", "start", "end"
# alongside the names of any optional keys which appeared in the attribute column

# open the file
def parse_gtf(fileParse, feature, fileDest):
    df = read_gtf(fileParse)
    # e.g df = read_gtf('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf')

    # filter of info based in the columns
    # df_genes = df[df["feature"] == "gene"]
    # df_exons = df[df["feature"] == "exon"]
    # df_introns = df[df["feature"] == "intron"]
    # df_cds = df[df["feature"] == "CDS"]
    # df_genes = df[df["feature"] == "gene"]

    # filter of info based in the columns
    # translate a DateFrame in array for manipulation
    str_genes = df[df["feature"] == feature].__array__()

    # str_genes = df[df["feature"] == "gene"].__array__()

    # get quantity of the genes and storage in the variable tam
    tam = len(str_genes)

    # open the file for write
    files_gene = open(fileDest, 'w')
    # e.g files_gene = open('C:/Users/breno/Desktop/gene.txt', 'w')

    # iterate by array and write in the file
    for i in range(0, tam - 1):
        for j in range(0, 25):
            # write the feature one an one
            # before insert a space bar for count the number de attr
            files_gene.write(str_genes[i][j].__str__())
            files_gene.write('|')
        # jump line in the file before write a position of the array
        files_gene.write('\n')
    files_gene.close()
