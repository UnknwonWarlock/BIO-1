# Contains some functions for general manipulations of strands
import os
import re

# param: a string for the desired strand
# return: the complement to the provided strand 
# sum: Gets the complement of the given strand.
# notes: 
#   Requires strand to be validated first
#   Function does no reverse for the direction
#   EX: if you give a 5->3 strand you will get the 3->5 complement and vice versa
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

# param: a string for the desired strand
# return: Reverse string for the strand
# sum: Reverses the direction of a given strand
# notes:
#   EX: If given 3->5 will return 5->3 and vice versa
def reverse(strand):
    return strand[::-1]

# param: A string for the desired strand
# return: either the validated strand or stops the programs execution
# sum: 
#   validates a provided strand to make sure it follows the following format:
#       1. Only contain A,T,C,G (meaning not empty too)
#       2. Is all uppercase (done within the function)
#       3. Contains no newlines (done within the function)
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