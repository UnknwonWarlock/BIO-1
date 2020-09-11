# Inlcudes anything used to get the primers
import os
import re
import strandmanipulation

def check_unique(primer, strand):
    pattern = re.compile(primer)
    result = pattern.search(strand)
    if result == None:
        return True
    else:
        return False

def get_primers(RNA)
