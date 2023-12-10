import re
import math

input = open("input.txt", "r")
input = input.readlines()
p = re.compile(r"\d+")

times = [41968894]
distances = [214178911271055]

def pq(p, q):
    p_half = (p / 2)
    p_half_sqr = p_half ** 2
    sqrt = math.sqrt(p_half_sqr -q)
    return (-p_half - sqrt, -p_half + sqrt)

def next_int(x):
    if x % 1 == 0:
        return x+1
    return math.ceil(x)

def f(t, d):
    a, b = pq(-t, d)
    a, b = (next_int(a), math.ceil(b))
    return b - a

product = 1
for (t, d) in zip(times, distances):
    product *= f(t, d)
print(product)