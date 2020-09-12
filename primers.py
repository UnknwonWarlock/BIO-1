# Inlcudes anything used to get the primers
import os
import strandmanipulation

# Param: a string for the desired primer and strand
# checks if the primer is unique in the provided strand
# Return: true if primer is unique otherwise false
def check_unique(primer, strand):
    result = strand.count(primer)
    if result == 1:
        return True
    else:
        return False

# Param: string for desired primer
# gets the gc count for the given primer
# Return: the gc count for the primer
def get_gc_count(primer):
    return (primer.count("G") + primer.count("C")) / len(primer)

# Param: an int for the length of a single strand, a tuple primer object for forward primer, a tuple primer object for reverse primer
# Both tuples for primers should be of (string, int int):
#       1. string: a string for the primer
#       2. int: first int is the inclusive start position for the primer in the strand
#       3. int: second int is the exclusive end position for the primer in the strand
# Calculates the distance between the primers
# Return: the distance between the primers
def get_distance(length, r_primer, f_primer):
    # remove parts not in the range
    distance = (length - f_primer[1]) - r_primer[1]
    
    # remove the size of the primers
    distance = (distance - len(f_primer[0]) - len(r_primer[0]))
    
    # add two for the two inclusive starts
    distance = distance + 2
    return distance

# Param: string for the desired strand, desired primer size, and inclusive start position
# gets a potential primer in the strand (tests for gc count and primer being unique in strand)
# the size of the primer retrieved by this function will be 20
# Return: a tuple of, the primer, its inclusive start position in the strand, and the exclusive end position
def get_potential_primer(strand, primer_size, start):
    # get the length of strand
    length = len(strand)
    
    # loop through strand until a potential primer is found
    while start < length:
        test = strand[start:start + primer_size]
        if check_unique(test, strand) and (get_gc_count(test) > 0.4 and get_gc_count(test) < 0.6) and len(test) == primer_size:
            return (test, start, start+primer_size)
        else:
            start = start + 1

# Param: a tuple of two complementary strands for cDNA, a limiter for the stopping condition, and the desired primer_size
# Gets a forward and reverse primers within inner range for the limiter
# Note: limiter is the inclusive outer range
# Return: tuple of the forward primer and revese primer tuples (See get_distance for details on primer tuples)
def get_primers(cDNA, limiter, primer_size):
    # get length from any of the single strands
    length = len(cDNA[0])

    # separate the two strands
    c_strand = cDNA[0]
    t_strand = cDNA[1]

    # get initial potential primers and distance
    f_primer = get_potential_primer(c_strand, primer_size, 0)
    r_primer = get_potential_primer(t_strand, primer_size, 0)
    distance = get_distance(length, r_primer, f_primer)

    # if not in the desired primers find new ones until they satisfy the limiter
    while distance > limiter:
        f_primer = get_potential_primer(c_strand, primer_size, f_primer[1] + 1)
        r_primer = get_potential_primer(t_strand, primer_size, r_primer[1] + 1)
        distance = get_distance(length, r_primer, f_primer)
    print("Returning Primers Have a Distance of: " + str(distance))
    return (f_primer, r_primer)