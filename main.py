# Introduction to Bioninformatics
# Project-1: Simulating PCR
# Project is meant to simulate PCR on an assigned Covid-19 gene.
# Assigned Gene: nsp6(YP_009725302.1) Range in Genome: [10973..11842]

import os
import strandmanipulation as smanip
import primers

# filename for the Covid-19 Genome
filename = "Files/SARS_COV2.fasta"

print()
print("Retrieving Genome from: " + filename)

# open the desired file
file = open(filename, "r")

# remove the first comment line
commentline = file.readline()

# reads in the whole genome into an object
# 5->3
genome = file.read()
genome = genome.replace("\n", "")

print("Issolating nsp6 gene from genome")
print()

# gets the nsp6 gene by using the provided range in the genome 
# 5->3
nsp6 = genome[10972:11842]

print("Validating nsp6 gene")

# validate nsp6
nsp6 = smanip.validate(nsp6)

# display the genes length and base pairs
print("nsp6 length: " + str(len(nsp6)))
print("nsp6:")
print(nsp6)
print()

print("Finding complement strand")

# retrieve complement strand to nsp6
# 3->5
c_nsp6 = smanip.getcomplement(nsp6)

# 5->3
c_nsp6 = smanip.reverse(c_nsp6)

# combine both strands together (coding strand, template strand)
# note: normally c_nsp6 would be going the opposite direction of nsp6 (EX: 5->3, 3->5) but for simplicity both strands go 5->3
cDNA = (nsp6, c_nsp6)
primers.get_primers(cDNA, 250)