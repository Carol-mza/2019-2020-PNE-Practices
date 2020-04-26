from Seq1 import *

print("-----| Practice 1, Exercise 9 |------")

file = "../Session 04/" + "U5.txt"

seq = Seq()
seq.read_fasta(file)
print()

print(f"Sequence: (Length: {seq.len()}) {seq}")
print(f"    Bases: {seq.count()}")
print(f"    Rev: {seq.reverse()}")
print(f"    Complement: {seq.complement()}")
print()