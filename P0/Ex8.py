from seq0 import *

file_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "G", "T"]

print("-----| Exercise 8 |-----")

for file in file_list:
    seq = seq_read_fasta('../Session 04/' + file + '.txt')
    dic = seq_count(seq)
    list_val = list(dic.values())
    m = max(list_val)
    print("Gene", file, ": Most frecuent base: ", base_list[list_val.index(m)], "appears-> ", m)