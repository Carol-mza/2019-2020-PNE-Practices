from Seq1 import *

print("-----| Practice 1, Exercise 8 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print()

list_seq = [seq1, seq2, seq3]

for seq in list_seq:
    print(f"Sequence {list_seq.index(seq)}: (Length: {seq.len()}) {seq}")
    print(f"    Bases: {seq.count()}")
    print(f"    Rev: {seq.reverse()}")
    print(f"    Complement: {seq.complement()}")
    print()