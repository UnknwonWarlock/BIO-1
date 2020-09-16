# Inlcudes anything used to get the primers
import os
import strandmanipulation as smanip

# param: a string for the desired primer and strand
# return: true if primer is unique otherwise false
# sum: checks if the primer is unique in the provided strand
def check_unique(primer, strand):
    result = strand.count(primer)
    if result == 1:
        return True
    else:
        return False

# param: string for desired primer
# return: the gc count for the primer
# sum: gets the gc count for the given primer
def get_gc_count(primer):
    return (primer.count("G") + primer.count("C")) / len(primer)


# param: starting position in the strand for the first primer, starting position in the strand for the second primer, primers' size
# return: the distance between the two primer's on the strand
# sum: Takes the length of the DNA strand subtract second position's primer to the first primer's position + the primer_size
# notes: make sure that primer_start_2 is farther primer in the strand
def get_distance(primer_start_1, primer_start_2, primer_size):
    return primer_start_2 - (primer_start_1 + primer_size)

    
# param: 
#   the strand that the primer should be found, the primer size to find, the primer size desired, the start, reverse the strand, and
#   complement flag to return the complement
#
# return: the primer found as a string or none
# sum: takes a strand and finds a potential primer to use
#
# notes: 
#   - if reverse is true reverses the given strand before working, if the complement is true the the returned result will be the
#     the complement of the actual result, false is default for both
#
#   - checks the gc count is >= 0.4 and <= 0.6, also checks the length, and that it is unique
def get_potential_primer(strand, primer_size=20, start=0, reverse=False, complement=False):
    working_strand = strand

    # reverse working strand if flag set
    if reverse:
        working_strand = smanip.reverse(strand)
    
    while start < len(strand):
        # get potential primer
        p_primer = working_strand[start: start + primer_size]

        # get current potential primer gc
        gc = get_gc_count(p_primer)

        # do some checks and return if valid, otherwise continue looping through strand
        if check_unique(p_primer, working_strand) and (gc >= 0.40 and gc <= 0.60) and len(p_primer) == primer_size:
            if complement:
                p_primer = smanip.getcomplement(p_primer)
            return p_primer
        else:
            start += 1


# param: 
#   DNA a tuple of two complementry strands, primer size, limiter to try and restrict distance for primers, reverse flag, 
#   complement flag, messages flag
#
# return: two primers found (forward 5->3, reverse 3->5) 
# sum: tries to find primers for the specified options and returns them 
# notes: 
#   - reverse and complement flags 0-3, 0 for none, 1 for forward primer, 2 for reverse primer, and 3 for both.
#     these help choose how the return output should be returned (all default is 0)
#
#   - messages flag turns on helpful messages for many of the potential primers found through the process
#     their distance and positions
#
#   - DNA is assumed to be (coding strand, template strand) and both going in the 3->5 direction
def get_primers(DNA, primer_size=20, limiter=200, reverse=0, complement=0, messages=True):

    # separate strand
    c_strand = DNA[0]
    t_strand = DNA[1]

    # get first primers
    f_primer = get_potential_primer(t_strand, primer_size, 0, False, True)
    r_primer = get_potential_primer(c_strand, primer_size, 0, False, True)
    r_primer = smanip.reverse(r_primer)

    # get primers' positions for distance
    primer_f_start = smanip.reverse(c_strand).index(f_primer)
    primer_r_start = t_strand.index(r_primer)

    # get distance
    distance = get_distance(primer_f_start, primer_r_start, primer_size)

    if messages:
        print("forward: " + f_primer)
        print("reverse: " + r_primer)
        print("primer_f_start: " + str(primer_f_start))
        print("primer_r_start: " + str(primer_r_start))
        print("distance: " + str(distance))
        print()

    # repeat above process until distance is less than limiter
    while distance > limiter:
        f_primer = get_potential_primer(t_strand, primer_size, primer_f_start + 1, False, True)
        r_primer = get_potential_primer(c_strand, primer_size, len(c_strand) - primer_r_start, False, True)
        r_primer = smanip.reverse(r_primer)

        primer_f_start = smanip.reverse(c_strand).index(f_primer)
        primer_r_start = t_strand.index(r_primer)

        distance = get_distance(primer_f_start, primer_r_start, primer_size)

        if messages:
            print("forward: " + f_primer)
            print("reverse: " + r_primer)
            print("primer_f_start: " + str(primer_f_start))
            print("primer_r_start: " + str(primer_r_start))
            print("distance: " + str(distance))
            print()

    if reverse == 1:
        f_primer = smanip.reverse(f_primer)
    elif reverse == 2:
        r_primer = smanip.reverse(r_primer)
    elif reverse == 3:
        f_primer = smanip.reverse(f_primer)
        r_primer = smanip.reverse(r_primer)

    if complement == 1:
        f_primer = smanip.getcomplement(f_primer)
    elif complement == 2:
        r_primer = smanip.getcomplement(r_primer)
    elif complement == 3:
        f_primer = smanip.getcomplement(f_primer)
        r_primer = smanip.getcomplement(r_primer)
    return (f_primer, r_primer)
