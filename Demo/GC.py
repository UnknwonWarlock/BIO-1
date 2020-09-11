# a python function
def get_GCcontent(dna):
    dna = dna.upper()
    return (dna.count("C")+dna.count("G"))/len(dna)


dna1 = "ATGaCGgaTCAGCCGcAAtACataCACTgttca"
print(get_GCcontent(dna1))
