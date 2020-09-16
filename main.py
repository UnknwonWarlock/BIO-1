# Introduction to Bioninformatics
# Project-1: Simulating PCR
# Project is meant to simulate PCR on an assigned Covid-19 gene.
# Assigned Gene: nsp6(YP_009725302.1) Range in Genome: [10973..11842]

import os
import strandmanipulation as smanip
import PCR as pcr
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
print("nsp6(5->3):")
print(nsp6)
print()

print("Finding complement strand for nsp6")

# retrieve complement strand to nsp6
# 3->5
c_nsp6 = smanip.getcomplement(nsp6)

# 5->3 to 3->5
nsp6 = smanip.reverse(nsp6)

# combine both strands together (coding strand, template strand)
# note: normally c_nsp6 would be going the opposite direction of nsp6 (EX: 5->3, 3->5) but for simplicity both strands go 3->5
print("Binding both nsp6 strands together")
cDNA = (nsp6, c_nsp6)

print("nsp6(3->5):")
print(nsp6)
print()
print("c_nsp6(3->5):")
print(c_nsp6)
print()

primes = primers.get_primers(cDNA, limiter=215, messages=False)
single_strands = pcr.denaturation([cDNA])
print("single_strands:")
print(single_strands)
pcr.annealing_elongation(single_strands, primes, 50, 205)

# forward:           ACCACTGGTTGTTACTCACA
# reverse:           ACGGACGATCAACCCACTAC
# primer_f_start:    31
# primer_r_start:    256
# distance:          205