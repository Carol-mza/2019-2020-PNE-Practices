from Seq1 import *

print("-----| Practice 1, Exercise 10 |------")

s = Seq()

file_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
seq_list =[]

base_list = ["A", "C", "G", "T"]

for file in file_list:
    seq_list.append(s.read_fasta('../Session 04/' + file + '.txt'))
    s = Seq()
    for seq in seq_list:
        dic = seq.count()
        list_val = list(dic.values())
        m = max(list_val)
    print("Gene", file, ": Most frecuent base: ", base_list[list_val.index(m)])