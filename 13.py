
import re

def horizontal(pattern):
    for i in range(1,len(pattern)):
        upper = pattern[:i][::-1]
        lower = pattern[i:]
        if sum(list(map(lambda a, b: sum([x is not y for (x, y) in zip(a,b)]), upper, lower))) == 1:
            return i
        
def transpose(pattern):
    return list(zip(*pattern))

input = [[l for l in re.findall(r"[#.]+", pattern)] for pattern in re.findall(r"(?:[#.]+\n)+", open("input.txt", "r").read())]
res = 0
for pattern in input:
    h = horizontal(pattern)
    if h:
        res += h * 100
    else:
        v = horizontal(transpose(pattern))
        if v:
            res += v
print(res)