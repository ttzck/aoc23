import re
import math
from collections import Counter
import copy



input = [(x, y) for y, l in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(l) if c == '#']
print(input)

k = 1000000
new_y = []
last_y = -1
expansion = 0
for x, y in input:
    if y - last_y > 1:
        expansion += (y - last_y - 1) * k - (y - last_y - 1)
    new_y.append(y + expansion)
    last_y = y
input = [(x, new_y[i]) for i, (x, y) in enumerate(input)]

input = sorted(input)
print(input)
new_x = []
last_x = -1
expansion = 0
for x, y in input:
    if x != last_x:
        expansion +=  (x - last_x - 1) * k - (x - last_x - 1)
    new_x.append(x + expansion)
    last_x = x
input = [(new_x[i], y) for i, (x, y) in enumerate(input)]

print(input)

sum = 0
for i, a in enumerate(input):
    for b in input[i+1:]:
        ax, ay = a
        bx, by = b
        sum += abs(ax - bx) + abs(ay - by)
print(sum)