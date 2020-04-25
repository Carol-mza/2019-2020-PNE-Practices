from seq0 import *

data = seq_read_fasta('../Session 04/' + 'U5.txt')
seq = data[:20]

print("-----| Exercise 7 |-----")
print(seq)
print(seq_complement(seq))