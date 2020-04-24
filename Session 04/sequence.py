from pathlib import Path

filename = "ADA.txt"
file = Path(filename)
data = file.read_text()

lines = data.split('\n')
body = ''.join(lines[1:])

print('The number of bases in the file {filename} is: ')
print(len(body))