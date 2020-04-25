from seq0 import *

list_file = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 5 |-----")

for file in list_file:
    seq = seq_read_fasta("../Session 04/" + file + ".txt")
    print("Gene ", file, ":", seq_count(seq))