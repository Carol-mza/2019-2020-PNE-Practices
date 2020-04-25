from seq0 import *

FOLDER = "../Session 04/"
filename = "U5.txt"
dna_file = FOLDER + filename
seq = seq_read_fasta(dna_file)
number_bases = 20

print("-----| Exercise 2 |-----")
print("DNA file:", filename)
print("The first ", number_bases, "are: ")
print(seq[:20])
