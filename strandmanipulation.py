# Contains some functions for general manipulations of strands
import os
import re

# Param: a string for the desired strand
# Gets the complement of the given strand.
# Requires strand to be validated first
# Function does no reverse for the direction
# EX: if you give a 5->3 strand you will get the 3->5 complement and vice versa
# Return: the complement to the provided strand 
def getcomplement(strand):


    # prints provided strand
    # Debugging Code
    #print("Given Strand:")
    #print(strand)

    # the needed replacements to get complement strand
    cStrand = strand.replace("A", "i")
    cStrand = cStrand.replace("C", "j")
    cStrand = cStrand.replace("T", "A")
    cStrand = cStrand.replace("G", "C")
    cStrand = cStrand.replace("j", "G")
    cStrand = cStrand.replace("i", "T")
    
    # print and return the found complement strand
    # Debugging Code
    #print()
    #print("Complement strand:")
    #print(cStrand)

    return cStrand

# Param: a string for the desired strand
# Reverses the direction of a given strand
# EX: If given 3->5 will return 5->3 and vice versa
# Return: Reverse string for the strand
def reverse(strand):
    return strand[::-1]

# Param: A string for the desired strand
# validates a provided strand to make sure it follows the following format:
# 1. Only contain A,T,C,G (meaning not empty too)
# 2. Is all uppercase (done within the function)
# 3. Contains no newlines (done within the function)
# Return: either the validated strand or stops the programs execution
def validate(strand):  
    strand = strand.replace("\n", "")
    strand = strand.upper()
    if re.search(r'[^ATCG]', strand) == None and len(strand) != 0:
        print("Valid Strand")
        return strand
    else:
        print("Invalid Strand Given:")
        print(strand)
        print()
        print("Stopping Execution")
        exit()