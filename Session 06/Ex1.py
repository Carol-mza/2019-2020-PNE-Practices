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

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")