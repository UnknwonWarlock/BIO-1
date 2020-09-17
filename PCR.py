# Contains functions to simulate PCR
import primers as prim
import random
import strandmanipulation as smanip

# param: a list of 2 string tuples to represent double stranded DNA
# return: a list of single stranded DNA
# sum: the double stranded list will be made into a list of single strands
# notes: this is the first step to PCR, which involves breaking the bonds of double strand DNA to make two separate strands
def denaturation(dna_list):
    single_strands = []
    for item in dna_list:
        single_strands.append(item[0])
        single_strands.append(item[1])
    return single_strands

# param: 
#   a list of single strands, the forward and reverse primers, the fall or rate (usually between -50 to 50), and the primers distance
#
# return: a list of two string tuples to represent double stranded DNA
# sum: attaches the appropriate primers and copies the segments
def annealing_elongation(single_strands, primers, fall_of_rate=50, primer_distance=200):
    DNA = []

    # get individual primers from primers
    f_primer = primers[0]
    r_primer = primers[1]

    # use any primer to get the length of a primer
    prim_length = len(f_primer)

    # calculate the rate for cycle
    rate = primer_distance + random.randint(-fall_of_rate, fall_of_rate)

    
    for item in single_strands:

        # first strand of the tuple DNA for the list is the initial single strand
        first = item
        second = ""
        
        if first == "":
            continue

        # if this is true then we are dealing with a reverse primer for the second
        if smanip.reverse(first).count(smanip.getcomplement(r_primer)) == 1:
            # easier to work with coding strands in 5->3
            second = smanip.reverse(first)

            # we need the complement to the r_primer to find the end index to get the strand we want the complement of
            check = smanip.getcomplement(r_primer)

            # get the end index
            end = second.index(check)

            # use end to get the strand we need the complement of and get the complement
            second = second[end - rate:end + prim_length]

            second = smanip.getcomplement(second)

        elif first.count(smanip.getcomplement(f_primer)) == 1:
            # no need to reverse since easier to work in 3->5
            second = first

            # need the complement of the primer to find start index on the strand
            check = smanip.getcomplement(f_primer)

            # use the complement to get the start index and find the part of the strand we want
            start = second.index(check)
            second = second[start: start + prim_length + rate]

            # get the complement and reverse the strand so we have 3->5 uniformly in every strand
            second = smanip.getcomplement(second)
            second = smanip.reverse(second)
            
        DNA.append((first,second))

    return DNA
    

def PCR(DNA, fall_of_rate, num_cycles,primers, primer_distance=200):
    cycles = 0
    PCRproducts = [DNA]
    while cycles < num_cycles:
        single_strands = denaturation(PCRproducts)
        PCRproducts = annealing_elongation(single_strands, primers, fall_of_rate, primer_distance)
        cycles += 1

    return PCRproducts