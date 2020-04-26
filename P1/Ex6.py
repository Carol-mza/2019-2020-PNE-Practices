from Seq1 import *

print("-----| Practice 1, Exercise 6 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print()

list_seq = [seq1, seq2, seq3]

for seq in list_seq:
    print(f"Sequence {list_seq.index(seq)}: (Length: {seq.len()}) {seq}")
    print(seq.count())
    print()