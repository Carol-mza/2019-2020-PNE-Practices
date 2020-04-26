class Seq:
    """A class for representing sequence objects"""
    Error = "ERROR!"
    Null = "NULL!"
    def __init__(self, strbases = Null):

        if strbases == self.Null:
            self.strbases = self.Null
            print("Null Seq created")
            return

        if not self.valid_seq(strbases):
            self.strbases = self.Error
            print("Invalid Seq!")
            return

        self.strbases = strbases
        print("New Seq created!")

    def valid_seq(strbases):
        bases = ["A", "C", "G", "T"]
        for b in strbases:
            if b not in bases:
                return False
        return True

    def __str__(self):       # Everytime we want to print an object
        return self.strbases

    def len(self):
        return len(self.strbases)
