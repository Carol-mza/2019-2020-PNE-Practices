from pathlib import Path

with open("RNU6_269P.txt", "r") as f:
    header = next(f)
    f.close()

file_contents = Path("RNU6_269P.txt").read_text()

print(file_contents)
