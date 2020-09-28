# Contains functions to simulate PCR
import primers as prim
import random
import strandmanipulation as smanip
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    c_f_primer = smanip.getcomplement(f_primer)

    r_primer = primers[1]
    c_r_primer = smanip.getcomplement(r_primer)
    c_r_primer = smanip.reverse(c_r_primer)

    # use any primer to get the length of a primer
    prim_length = len(f_primer)


    for item in single_strands:

        # calculate the rate strand cycle
        rate = random.randint((primer_distance + (2 * prim_length)) - fall_of_rate, (primer_distance + (2 * prim_length)) + fall_of_rate)

        # first strand of the tuple DNA for the list is the initial single strand
        first = item
        second = ""

        if first == "":
            continue

        # if this is true then we are dealing with a reverse primer for the second
        if first.find(c_r_primer) != -1:
            # easier to work with coding strands in 5->3
            second = first

            # we need the complement to the r_primer to find the end index to get the strand we want the complement of
            check = c_r_primer

            # get the end index
            end = second.index(check)

            # use end to get the strand we need the complement of and get the complement
            second = second[end:end + prim_length + rate]

            second = smanip.getcomplement(second)
            second = smanip.reverse(second)

        elif first.find(c_f_primer) != -1:
            # no need to reverse since easier to work in 3->5
            second = first

            # need the complement of the primer to find start index on the strand
            check = c_f_primer

            # use the complement to get the start index and find the part of the strand we want
            start = second.index(check)

            second = second[start: start + prim_length + rate]

            # get the complement and reverse the strand so we have 3->5 uniformly in every strand
            second = smanip.getcomplement(second)
            second = smanip.reverse(second)

        DNA.append((first,second))

    return DNA

# param: 
#   DNA a list of double strand tuples, the e aspect of the fall off rate, the number of cycles desired, 
#   a tuple containing the (forward, reverse) primers, and the distance between the primer
#
# return: the products of the PCR, list of double strand tuples
# sum: Will simulate PCR on the provided DNA with the given cycles
# notes: primers should be (forward 5->3, reverse 3->5)
def PCR(DNA, fall_of_rate, num_cycles,primers, primer_distance=200, cycle_messages=True):
    cycles = 0
    PCRproducts = [DNA]
    while cycles < num_cycles:
        single_strands = denaturation(PCRproducts)
        PCRproducts = annealing_elongation(single_strands, primers, fall_of_rate, primer_distance)
        if cycle_messages:
            print("Cycle " + str(cycles+1) + ": Completed")
        cycles += 1

    return PCRproducts


# param: the results of the PCR simulation, a max value to use for the minimum check, a with_originals bool flag, a log bool flag
# returns: none
# sum: prints some statistics about the data given
# notes: 
#   The with_originals flag when false will search for the original two strands and not use them for the calculations
#   The log flag will set the graph to a log scale for the y axis
def get_stats(results, max=1000000, with_originals=False, log=False):
    avg_gc = 0
    avg_length = 0
    min_length = max
    max_length = 0
    DNA_fragments = 0
    single_strands = 0
    double_strands = 0
    bar_chart = {}

    # calculation with original two strands
    if with_originals:
        for items in results:

            # Check if a second strand exist or not
            if items[1] == "":

                # fill dictionary with strand lenghts and counts for length distribution
                if len(items[0]) in bar_chart:
                    bar_chart[len(items[0])] +=  1
                else:
                    bar_chart[len(items[0])] = 1

                # add 1 to single strand count
                single_strands += 1

                # update the totals for gc and length
                avg_gc += prim.get_gc_count(items[0])
                avg_length += len(items[0])

                # check if new min and max
                if len(items[0]) < min_length:
                    min_length = len(items[0])

                if len(items[0]) > max_length:
                    max_length = len(items[0])

            else:

                # fill dictionary with strand lenghts and counts for length distribution
                if len(items[0]) in bar_chart:
                    bar_chart[len(items[0])] +=  1
                else:
                    bar_chart[len(items[0])] = 1

                if len(items[1]) in bar_chart:
                    bar_chart[len(items[1])] +=  1
                else:
                    bar_chart[len(items[1])] = 1

                # double strand otherwise
                double_strands += 1

                # update total length and gc
                avg_gc += (prim.get_gc_count(items[0]) + prim.get_gc_count(items[1]))
                avg_length += (len(items[0]) + len(items[1]))

                # check both strands for new max and min
                if len(items[0]) < min_length:
                    min_length = len(items[0])
                if len(items[1]) < min_length:
                    min_length = len(items[1])

                if len(items[0]) > max_length:
                    max_length = len(items[0])
                if len(items[1]) > max_length:
                    max_length = len(items[1])
    else:
        # get original size of first strands. One should be the first element of the first tuple
        original_size = len(results[0][0])
        for items in results:

            # Check if a second strand exist or not
            if items[1] == "":
                # single strand if it doesn't
                single_strands += 1

                # check if the single strand is not an original
                if len(items[0]) != original_size:

                    # fill dictionary with strand lenghts and counts for length distribution
                    if len(items[0]) in bar_chart:
                        bar_chart[len(items[0])] +=  1
                    else:
                        bar_chart[len(items[0])] = 1

                    # if it is not an original we can check and update values appropriately
                    avg_gc += prim.get_gc_count(items[0])
                    avg_length += len(items[0])

                    if len(items[0]) < min_length:
                        min_length = len(items[0])

                    if len(items[0]) > max_length:
                        max_length = len(items[0])

            else:
                # double strand otherwise
                double_strands += 1

                # check if the first strand is not an original
                if len(items[0]) != original_size:

                    # fill dictionary with strand lenghts and counts for length distribution
                    if len(items[0]) in bar_chart:
                        bar_chart[len(items[0])] +=  1
                    else:
                        bar_chart[len(items[0])] = 1

                    if len(items[1]) in bar_chart:
                        bar_chart[len(items[1])] +=  1
                    else:
                        bar_chart[len(items[1])] = 1

                    # check and update values appropriately if it isn't
                    avg_gc += prim.get_gc_count(items[0])
                    avg_length += len(items[0])

                    if len(items[0]) < min_length:
                        min_length = len(items[0])

                    if len(items[0]) > max_length:
                        max_length = len(items[0])

                # check if second strand is not an original
                if len(items[1]) != original_size:

                    # if it is not check and update values appropriately
                    avg_gc += prim.get_gc_count(items[1])
                    avg_length += len(items[1])

                    if len(items[1]) < min_length:
                        min_length = len(items[1])
                    if len(items[1]) > max_length:
                        max_length = len(items[1])

    DNA_fragments = single_strands + (2 * double_strands)
    avg_gc = avg_gc / DNA_fragments
    avg_length = avg_length / DNA_fragments

    print("=====================Statistics=====================")

    if with_originals:
        print("Statistics Calculated with the Original Two Strands!")
    else:
        print("Statistics Calculated WITHOUT the Original Two Strands!")

    print("DNA Fragments: " + str(DNA_fragments))
    print("Single Strands: " + str(single_strands))
    print("Double Strands: " + str(double_strands))
    print("Maximum Strand Length: " + str(max_length))
    print("Minimum Strand Length: " + str(min_length))
    print("Average Strand Length: " + str(avg_length))
    print("Average Strand GC Count: " + str(avg_gc * 100))
    plt.xlabel("Sizes")
    plt.ylabel("Counts")

    if log:
        plt.yscale("log")

    plt.title("Size Distributions")
    plt.bar(bar_chart.keys(), bar_chart.values())
    plt.show()
