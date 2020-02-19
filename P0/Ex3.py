from seq0 import *

FOLDER = "../Session 04/"
list_file = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("----- | EXERCISE 3 | -----")
for file in list_file:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene", file, "---> Lenght: ", len_seq(sequence))
