from seq0 import *

FOLDER = "../Session 04/"
filename = "U5.txt"
number_bases = 20

print("DNA file:", filename)
print("The first ", number_bases, "are: ")
print(seq_read_fasta(FOLDER + filename)[:number_bases])
