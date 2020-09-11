

# param: a double strand dna, a tuple of 2 strings, representing 2 segments of dna from 5" to 3"
# return: a tuple of 2 strs representing the pair of primers (5" -> 3", GC content > 40%, bases btw the 2 primers: ~200)
def getPrimers(dna_segment):
    # ....
    primers = ()  # (forward_primer, reverse_primer)
    return primers


# param: a single strand 5" to 3" dna
# return: a single strand 5" to 3" dna that is reverse complement to the input strand
def reverse_complement(dna5_3):  # input is a strand from 5" to 3"
    rc_dna5_3 = dna5_3.replace('A', 'X')  # replace A by X
    rc_dna5_3 = rc_dna5_3.replace('T', 'A')  # replace T by A
    rc_dna5_3 = rc_dna5_3.replace('X', 'T')  # replace X by A
    rc_dna5_3 = rc_dna5_3.replace('C', 'X')  # replace C by X
    rc_dna5_3 = rc_dna5_3.replace('G', 'C')
    rc_dna5_3 = rc_dna5_3.replace('X', 'G')
    rc_dna5_3 = rc_dna5_3[::-1]  # reverse the complementary strand to have a strand from 5" to 3"
    return rc_dna5_3


# param: a list of tuples of 2 strs, representing double stranded dna segments
# return: a list of single strand dna segments
def denaturation(dna_segments):
    singleStrandDNAs = []
    return singleStrandDNAs


# param: a list of single strand dna segments, each segment is from 5" to 3"
# return: a list of tuples of 2 strs (2 dna segments from 5" to 3")
def annealing_elongation(singleStrandDNAs, primers, fall_of_rate):
    # ...
    doubleStrandedDNAs = [('a','a'),('a','a')]  # get your sequence of dnas
    return doubleStrandedDNAs


# param: gene to be copied (a tuple of 2 strs), fall of rate of DNA polymerase (int), and num_cycles to run PCR (int)
# return: a list of double stranded dna segments
def PCR(dna_segment_to_be_copied, fall_of_rate, num_cycles):
    # ....
    primers = getPrimers(dna_segment_to_be_copied)
    cycles = 0
    PCRproducts = [dna_segment_to_be_copied]
    while cycles < num_cycles:
        singleStrandDNAs = denaturation(PCRproducts)
        PCRproducts = annealing_elongation(singleStrandDNAs, primers, fall_of_rate)

    return PCRproducts


# param: a list of tuples of 2 strings representing double stranded DNA segments
# return: null
def getStats(PCR_products):
    # ...
    print()
    return


# the gene needs to be amplified
S_gene = "ATG..."
cDNA_S = reverse_complement(S_gene)
rccDNA_S = S_gene

# It is the double strand DNA {cDNA_S, rccDNA_S} that can be amplified.
DNA_S = (cDNA_S, rccDNA_S)

fall_of_rate = 50  # between -50 to 50
num_cycles = 20  # PCR cycles

# call PCR function to simulation the PCR process
PCR_products = PCR(DNA_S, fall_of_rate, num_cycles)

# print stats of PCR_products
getStats(PCR_products)

