# Contains functions to simulate PCR
import primers

# Param: a list of 2 string tuples to represent double stranded DNA
# the double stranded list will be made into a list of single strands
# this is the first step to PCR, which involves breaking the bonds of double strand DNA to make two separate strands
# Return: a list of single stranded DNA
def denaturation(dna_list):
    single_strands = []
    for item in dna_list:
        single_strands.append(item[0])
        single_strands.append(item[1])
    return single_strands

# Param: a list of single strands, the forward and reverse primers, the fall or rate (usually between -50 to 50)
# attaches the appropriate primers and copies the segments
# Return: a list of two string tuples to represent double stranded DNA
def annealing_elongation(single_strands, primers, fall_of_rate):
    print()

def PCR(DNA, fall_of_rate, num_cycles, limiter=215, primer_size=22):
    primers = primers.get_primers(DNA,limiter,primer_size)
    cycles = 0
    PCRproducts = [DNA]
    while cycles < num_cycles:
        single_strands = denaturation(PCRproducts)
        PCRproducts = annealing_elongation(single_strands, primers, fall_of_rate)
        cycles += 1

    return PCRproducts