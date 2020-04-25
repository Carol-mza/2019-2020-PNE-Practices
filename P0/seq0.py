from pathlib import Path

def seq_ping():
    print("OK!")

def seq_read_fasta(filename):
    # -- Open and read the file
    file = Path(filename)
    file_contents = file.read_text()
    lines = file_contents.split('\n')
    content = "".join(lines[1:])
    return content

def len_seq(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    res = {"A" : seq_count_base(seq, "A"), "C" : seq_count_base(seq, "C"),
           "G" : seq_count_base(seq, "G"), "T" : seq_count_base(seq, "T")}
    return res

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    # It can also be done with dictionaries
    res = ''
    for i in seq:
        if i == 'A':
            res = res + 'T'
        elif i == 'T':
            res = res + 'A'
        elif i == 'C':
            res = res + 'G'
        elif i == 'G':
            res = res + 'C'
    return res