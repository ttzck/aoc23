import re

input = open("input.txt", "r")
sum = 0
p = re.compile(r"(\d+)\s(\w+)")


def min_power(m):
    r, g, b = [0, 0, 0]
    for n, c in m:
        n = int(n)
        if c == 'red' and n > r: 
            r = n
        elif c == 'green' and n > g: 
            g = n
        elif c == 'blue' and n > b: 
            b = n
    return r * g * b


for l in input:
    m = re.findall(p, l)
    sum += min_power(m)
print(sum)