import os
file = open('SARS_COV2.fasta', 'r')
comments = file.readline()
SARS_COV2_genome = file.read()
file.close()
SARS_COV2_genome = SARS_COV2_genome.replace('\n','')

# extract spike gene from 21563:25384
S_gene = SARS_COV2_genome[21562:25384]   # rna sequence

