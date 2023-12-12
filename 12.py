
import re


def group_fits_at(size, i, row):
    return (
        i + size <= len(row) # group fits in rows length
        and (i == 0 or row[i-1] in ['.', '?']) # before i is free space
        and all(x in ['#', '?'] for x in row[i:i+size]) # springs can be placed in [i, i+size)
        and (i + size == len(row) or row[i+size] in ['.', '?']) # after i + size is free space
    )

def f(i, groups, row):
    if groups == []: 
        return 1
    sum = 0
    for j in range(i, len(row)):
        if group_fits_at(groups[0], j, row):
            sum += f(j + groups[0] + 1, groups[1:], row)
        if row[j] == '#': break
    return sum


input = [re.match(r"([?.#]+) ([\d,]*)", l).groups() for l in open("input.txt", "r").readlines()]
input = [(r, [int(i) for i in re.findall(r'\d+', g)]) for (r, g) in input]
arrangements = [f(0, g, r) for (r, g) in input]
print(sum(arrangements))
#print(f(0, [3], '?###????????'))