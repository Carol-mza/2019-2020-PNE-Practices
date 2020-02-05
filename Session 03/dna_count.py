dna = input("Introduce the DNA sequence: ")

a = 0
g = 0
t = 0
c = 0
length = 0

for i in dna:
    length += 1
    if i == "A":
        a += 1
    elif i == "C":
        c += 1
    elif i == "G":
        g += 1
    elif i == "T":
        t += 1

print("Total length: ", length)
print("A: ", a)
print("C: ", c)
print("T: ", t)
print("G: ", g)