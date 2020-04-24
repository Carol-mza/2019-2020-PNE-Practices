from pathlib import Path

file = Path("dna.txt")
data = file.read_text()

print("File: ", file)
print("Data: ", data)

length = 0
a = 0
c = 0
g = 0
t = 0
unknown = 0

for i in data:
    if i == "A":
        a += 1
    elif i == "C":
        c += 1
    elif i == "G":
        g += 1
    elif i == "T":
        t += 1
    else:
        unknown += 1

length = a + c + t + g

print("Total length: ", length)
print("A: ", a)
print("C: ", c)
print("T: ", t)
print("G: ", g)