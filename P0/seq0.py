import pathlib

def seq_ping():
    print("OK!")

def seq_read_fasta(filename):
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    content = "".join(file_contents)
    return content

def len_seq(seq):
    return len(seq)

