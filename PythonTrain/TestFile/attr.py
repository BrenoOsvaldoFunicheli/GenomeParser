source = open('C:/Users/breno/Desktop/Homo_sapiens.GRCh38.91.gtf', 'r')
intermediate = open('C:/Users/breno/Desktop/intermediateParse.gtf', 'w')

# iterates through several lines by
# taking each line of the file and
# writing in the other file
for x in range(10000):
    text = source.readline()
    intermediate.write(text)
    #print(text)

# close the files
source.close()
intermediate.close()

# open the file with a
# df = read_gtf('C:/Users/breno/Desktop/intermediateParse.gtf')
# df = parse_gtf_and_expand_attributes('C:/Users/breno/Desktop/intermediateParse.gtf')


#attr standard of the files GTF

# seqname = df_genes['seqname']
# source = df_genes['source']
# feature = df_genes['feature'] translate in tables
# start = df_genes['start']
# end = df_genes['end']
# score = df_genes['score']
# strand = df_genes['strand']
# frame = df_genes['frame']

# other attributes caracteristic of the file

# gene_id = df_genes['gene_id'].__array__()
# gene_version = df_genes['gene_version'].__array__()
# gene_name = df_genes['gene_name'].__array__()
# gene_source = df_genes['gene_source'].__array__()
# gene_biotype = df_genes['gene_biotype'].__array__()
# transcript_id = df_genes['transcript_id'].__array__()
# transcript_version = df_genes['transcript_version'].__array__()
# transcript_name = df_genes['transcript_name'].__array__()
# transcript_source = df_genes['transcript_source'].__array__()
# transcript_biotype = df_genes['transcript_biotype'].__array__()
# tag = df_genes['tag'].__array__()
# transcript_support_level = df_genes['transcript_support_level'].__array__()
# exon_number = df_genes['exon_number'].__array__()
# exon_id = df_genes['exon_id'].__array__()
# exon_version = df_genes['exon_version'].__array__()
# ccds_id = df_genes['ccds_id'].__array__()
# protein_id = df_genes['protein_id'].__array__()
# protein_version = df_genes['protein_version'].__array__()

'''
genes = df_genes[df_genes["feature"] == "gene"]
exons = df_genes[df_genes["feature"] == "exon"]
introns = df_genes[df_genes["feature"] == "intron"]
CDSs = df_genes[df_genes["feature"] == "CDS"]

#['gene_id', 
# 'gene_version', 
# 'gene_name', 
# 'gene_source',
# 'gene_biotype', 
# 'transcript_id', 
# 'transcript_version',
# 'transcript_name', 
# 'transcript_source', 
# 'transcript_biotype',
# 'tag', 
# 'transcript_support_level',
# 'exon_number',
# 'exon_id', 
# 'exon_version', 
# 'ccds_id', 
# 'protein_id', 
# 'protein_version'
'''