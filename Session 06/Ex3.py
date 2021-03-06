class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        bases = ["A", "C", "G", "T"]
        for b in strbases:
            if b not in bases:
                print("ERROR!")
                self.strbases = "ERROR"
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):       # Everytime we want to print an object
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seqs):
    for seq in seqs:
        print(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}")

def generate_seqs(pattern, number):
    seqs = []
    for i in range(1, number + 1):
        seqs.append(Seq(pattern * i))
    return seqs

list_seq1 = generate_seqs("A", 3)
list_seq2 = generate_seqs("AC", 5)

print("List 1")
print_seqs(list_seq1)
print()

print("List 2")
print_seqs(list_seq2)