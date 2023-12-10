import re

n = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
input = open("1-2-input.txt", "r")
sum = 0
p = re.compile(f"(?=([0-9]|{'|'.join(n)}))")


def digit(x):
    if x in n:
        return n.index(x) + 1
    return int(x)


for l in input:
    m = re.findall(p, l)
    sum += digit(m[0]) * 10 + digit(m[-1])
print(sum)

