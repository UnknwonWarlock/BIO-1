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

- get_distance(length, r_primer, f_primer)
  - given the length of the full strand, an reverse primer tuple, and a forward primer tuple and returns the distance between the two
  - the primer tuples are formatted as (string, int, int)
    - the string is the primer
    - the first int is the inclusive start point
    - the second int is the exclusive end point

- get_potential_primer(strand, primer_size, start)
  - given the full strand, the desired primer size (typically between 18-24), and the inclusive start point to search from it will return a primer tuple or none.
  - Whether this is the reverse or forward primer depends on the strand given and is up to the user to determine
  - keeping track of the direction is also up to the user of the function
  - Notes: to use the get_distance function the primer tuples provided assume the the int start and int end of from the two primers are from the same direction in this function (both strands where inserted into the function going the same direction, either both 5->3 or 3->5)
