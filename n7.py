import csv
import sys
import fugashi
from collections import defaultdict
import gzip

def is_swappable(pos1, form):
    if pos1 in ("名詞", "接尾辞", "形容詞", "形容動詞", "動詞", "形状詞"):
        return True
    return False

def read_csv(fname):
    with open(fname) as infile:
        return read_file(infile)

def read_gz(fname):
    with gzip.open(fname, 'rt') as infile:
        return read_file(infile)

def read_file(infile):
    ref = defaultdict(list)
    for line in csv.reader(infile):
        surface = line[0]
        pos1 = line[4]
        form = line[9]
        if not is_swappable(pos1, form): continue

        ref[(pos1, form)].append(surface)

    return ref

def swap_term(ref, node, offset=230):
    surf = node.surface
    pos1 = node.feature.pos1
    form = node.feature.cForm
    key = (pos1, form)

    ll = len(ref[key])
    try:
        ii = ref[key].index(surf)
    except ValueError:
        ii = hash(surf) % ll
    ni = (ii + offset) % ll

    return ref[key][ni]

def swap_line(tagger, ref, text):
    out = []
    for node in tagger(text):
        surf = node.surface
        if is_swappable(node.feature.pos1, node.feature.cForm):
            surf = swap_term(ref, node)
        out.append(surf)
    return ''.join(out)

        
if __name__ == '__main__':
    tagger = fugashi.Tagger()
    ref = read_csv(sys.argv[1])

    while True:
        text = input("input> ")
        out = swap_line(tagger, ref, text)
        print(out)
        print()



