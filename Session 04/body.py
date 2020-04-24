from pathlib import Path

filename = "U5.txt"
file = Path(filename)
data = file.read_text()

with open("U5.txt", 'r') as f:
    next(f)
    print(f.read())
    f.close()

lines = data.split('\n')
body = '\n'.join(lines[1:])

print()
print(f'Body of the {filename} file:')
print(body)