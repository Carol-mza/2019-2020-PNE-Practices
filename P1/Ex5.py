from Seq1 import *

print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print()

for i, seq in enumerate([seq1, seq2, seq3]):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    for b in ["A", "C", "G", "T"]:
        print(f"    {b}: {seq.count_base(b)}", end = ', ')
    print()