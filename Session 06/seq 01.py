class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):       # Everytime we want to print an object
        return self.strbases

    def len(self):        # Always self inside so we know is of the method
        return len(self.strbases)


class Gene(Seq):

    pass

# -- Main program
s1 = Seq("AACGTC")
g = Gene("ACCTGA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {g}")

l1 = s1.len()
l2 = g.len()

print(f"The length of the sequence 1 is {l1}")
print(f"The length of the sequence 2 is {g.len()}")

