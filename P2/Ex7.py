from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 7 |-----")

ip = "192.168.1.45"
port1 = 8080
port2 = 8081

c1 = Client(ip, port1)
c2 = Client(ip, port2)

print(c1)
print(c2)

folder = "../Session 04/"
file = "FRAT1.txt"

seq = Seq().read_fasta(folder + file)
length = 10

msg = f"Sending FRAT1 gene to the server in fragments of {length} bases..."
c1.talk(msg)
c2.talk(msg)

print(f"Gene FRAT1: {str(seq)}")

for i in range(10):
    frag = str(seq)[i * length: (i+1) * length]
    print(f"Fragment {i+1}: {frag}")
    m = f"Fragment {i+1}: {frag}"
    if i % 2:
        c2.talk(m)
    else:
        c1.talk(m)