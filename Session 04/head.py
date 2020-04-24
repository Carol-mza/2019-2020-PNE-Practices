from pathlib import Path

with open("RNU6_269P.txt", "r") as f:
    header = next(f)
    f.close()

print(header)

filename = "RNU6_269P.txt"
file = Path(filename)
data = file.read_text()

line = data.split('\n')

print(line[0])