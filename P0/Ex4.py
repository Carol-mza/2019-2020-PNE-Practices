from seq0 import *

list_file = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
list_bases = ["A", "C", "G", "T"]

print("------| Exercise 5 |-----")
for file in list_file:
    seq = seq_read_fasta("../Session 04/" + file + ".txt")
    print("Gene ", file, ":")
    for base in list_bases:
        print(base, ":", seq_count_base(seq, base))

    print()