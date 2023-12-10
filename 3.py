import re
from collections import defaultdict 

input = open("3-2-input.txt", "r")
sum = 0
p1 = re.compile(r"(\d+)")
p2 = re.compile(r"(\*)")
x = ['.' + l[0:-1] + '.' for l in input.readlines()]
x = ['.' * len(x)] + x + ['.' * len(x)]
gears = defaultdict(list)

def f(i, s, e, n):
    for m in re.finditer(p2, x[i][s:e]):
        gears[(i, s + m.start())].append(n)

for i, l in enumerate(x):
    for m in re.finditer(p1, l):
        n = int(m.group(0))
        f(i-1, m.start()-1, m.end()+1, n)
        f(i  , m.start()-1, m.end()+1, n)
        f(i+1, m.start()-1, m.end()+1, n)

for g in gears:
    if len(gears[g]) == 2:
        sum += gears[g][0] * gears[g][1]

print(sum)