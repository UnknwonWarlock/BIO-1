# BIO-1

University of Akron  
Dr. Duan  
Introduction to Bioinformatics: Project 1 PCR Simulation  
  
Project is meant to simulate PCR on the Covid-19 genome to an assigned gene. The assigned gene for the groups is: nsp6

## nsp6

ID: YP_009725302.1  
Range(In Genome): [10973..11842]

## Code

### strandmanipulation

Contains functions for some basic but useful manipulation to stingle strands. This includes:

- getcomplement(strand)
  - gets the complement of the given strand (does not reverse the direction)

- reverse(strand)
  - reverses the direction of a given strand

- validate(strand)
  - validates the provided strand (will remove newlines and make all the characters capital letters)
  - any other issues that may be found will stop the execution of the program

### primers

Contains functions for some functions to help find and tune the desired aspect of the primers. Includes:

- check_unique(primer, strand)
  - takes in a potential primer and the strand to check it against
  - will return true if the primer is unique in the strand and false otherwise

- get_gc_count(primer)
  - given a potential primer it will return the GC count. In this project we want a GC count between 0.40 and 0.60

- get_distance(primer_start_1, primer_start_2, primer_size)
  - given the start position of the forward primer, the start position in the reverse primer, and the primer size. The distance between the two primer positions will be returned

- get_potential_primer(strand, primer_size, start, reverse, complement)
  - given the full strand, the desired primer size (typically between 18-24), and the inclusive start point to search from it will return a primer or none.
  - Whether this is the reverse or forward primer depends on the strand given and is up to the user to determine
  - keeping track of the direction is also up to the user of the function
  - There is also to option flags:
    - reverse says whether or not to reverse the strand given before finding the primer
    - complement says whether to return the resulting primer's complement or not

- get_primers(DNA, primer_size=20, limiter=200, reverse=0, complement=0, messages)
  - given the double stranded DNA, the desired primer sie, a limiter to try and reduce the distance, a reverse flag, a complement flag, and a messages flag
  - function will find primers with the desired parameters and return them (forward, reverse)
  - reverse and complement have four options: 0-3
    - 0 says none of the results should have these applied
    - 1 says the forward primer should have these applied
    - 2 says the reverse primer should have these applied
    - 3 says both the primers should have these applied
  - the message flag enables and disables messages about the found primer and some information. This allows the user to look through many primers and dicide which ones they would prefer.

#### Primer Function Notes

- Very rough way of doing this

### PCR

Contains functions to help simulate the PCR process. Includes:

- denaturation(dna_list)
  - Takes a list of double stranded DNA and splits them into a list of single stranded DNA and returns them

- annealing_elongation(single_strands, primers, fall_of_rate=50, primer_distance=200)
  - Takes a list of single stranded DNA, the two primer (forward 5->3, reverse 3->5), the e part of the fall off rate (d+e where e can be [-e:e]), and the primer distance (d of d+e)
  - This will attach the primers and make a copy of a segment of DNA based on the fall of rate
  - This can fail if the primers don't attach, leaving a blank strand
  - returns the products as a list of double stranded DNA

- PCR(DNA, fall_of_rate, num_cycles,primers, primer_distance=200)
  - Takes a list of double stranded DNA, the two primer (forward 5->3, reverse 3->5), the e part of the fall off rate (d+e where e can be [-e:e]), and the primer distance (d of d+e), and the number of cycles to repeat the PCR process
  - returns the products of the resulting repeats in the denaturation, annealing, and elongation cycle

- get_stats(results, max, with_originals)
  - given the results from PCR, a max to use to get the minimum, and the with_original flags
  - Will calculate and print results for several statistics:
    - Average GC count
    - Average length
    - Maximum length
    - Minimum length
    - Total DNA strands
    - How many entries were single strands
    - How many entries were double strands
    - Display a bar chart of the length distributions for the strands
  - the with_original flag says whether to include the two original DNA strands in the stat calculations or not
  - The max really only has to be as big as the original strand size
