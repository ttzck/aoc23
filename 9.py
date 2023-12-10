import re
import math
from collections import Counter

input = open("input.txt", "r") .readlines()
p = re.compile(r"-?\d+")
input = [[int(x) for x in re.findall(p, l)] for l in input]


# old solution
def deconstruct(seq):
    seqs = [seq]
    if any(map(lambda x: x != 0, seq)):
        next_seq = []
        for i in range(1, len(seqs[-1])):
            next_seq.append(seq[i] - seq[i-1])
        seqs.extend(deconstruct(next_seq))
    return seqs


def expand_all(seqs):
    seqs = list(reversed(seqs))
    seqs[0].insert(0, 0)
    for i in range(1, len(seqs)):
        seqs[i].insert(0, seqs[i][0] - seqs[i-1][0])
    return seqs

# new solution inspired by reddit
def extrapolate(seq):
    if all(x == 0 for x in seq):
        return 0
    return seq[-1] + extrapolate([b - a for (a, b) in zip(seq, seq[1:])])

print("part 1:", sum(map(extrapolate, input)))
print("part 2:", sum(map(lambda x: extrapolate(x[::-1]), input)))
