# Contains some functions for general manipulations of strands
import os
import re

# provides a single strand of DNA and provides the complement
# requires a valid strand be passed
# this function does not reverse the order
# EX: if you give a 5->3 strand you will get the 3->5 complement and vice versa
def getcomplement(strand):


    # prints provided strand
    print("Given Strand:")
    print(strand)

    # the needed replacements to get complement strand
    cStrand = strand.replace("A", "i")
    cStrand = cStrand.replace("C", "j")
    cStrand = cStrand.replace("T", "A")
    cStrand = cStrand.replace("G", "C")
    cStrand = cStrand.replace("j", "G")
    cStrand = cStrand.replace("i", "T")
    
    # print and return the found complement strand
    print()
    print("Complement strand:")
    print(cStrand)

    return cStrand

# reverse a provided strand
# if given 3->5 will return 5->3 and vice versa
def reverse(strand):
    return strand[::-1]

# validates a provided strand to make sure it follows the following format:
# 1. Only contain A,T,C,G (meaning not empty too)
# 2. Is all uppercase (done within the function)
# 3. Contains no newlines (done within the function)
# if it is valid it will return the validated string else will return false
def validate(strand):  
    strand = strand.replace("\n", "")
    strand = strand.upper()
    if re.search(r'[^ATCG]', strand) == None and len(strand) != 0:
        return strand
    else:
        return False
