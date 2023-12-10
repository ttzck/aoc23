import re
import math
from collections import Counter
import copy


def opposite(dir):
    i = directions.index(dir)
    return directions[(i + 2) % len(directions)]


def pipe_at(x, y):
    if x < 0: return '.'
    if x >= len(input[0]): return '.'
    if y < 0: return '.'
    if y >= len(input): return '.'
    
    return input[y][x]


def part1(sx, sy):
    visited = []
    q = [(sx, sy, 0)]
    s = []
    while q:
        x, y, steps = q.pop(0)
        if (x, y) in visited:
            continue

        visited.append((x,y))
        p = pipe_at(x, y)
        for d in allowed_directions[p]:
            dx, dy = translations[d]
            if pipe_at(x + dx, y + dy) in allowed_pipes[opposite(d)]:
                s.append(steps)
                q.append((x + dx, y + dy, steps + 1))
    return max(s)

def mark_loop(sx, sy):
    visited = []
    q = [(sx, sy, 0)]
    while q:
        x, y, steps = q.pop(0)
        if (x, y) in visited:
            continue

        visited.append((x,y))
        p = pipe_at(x, y)
        for d in allowed_directions[p]:
            dx, dy = translations[d]
            if pipe_at(x + dx, y + dy) in allowed_pipes[opposite(d)]:
                q.append((x + dx, y + dy, steps + 1))
    return visited


input = [list(l[:-1]) for l in open("input.txt", "r").readlines()]

directions = ['n', 'e', 's', 'w']
pipes = ['|', '-', 'L', 'J', '7', 'F']

translations = {
    'n' : (0, -1),
    'e' : (1, 0),
    's' : (0, 1),
    'w' : (-1, 0),
}

allowed_directions = {
    'S': ['n', 'e', 's', 'w'],
    '|': ['n', 's'],
    '-': ['e', 'w'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['s', 'e'],
    }

allowed_pipes = {d:[p for p in pipes if d in allowed_directions[p]] for d in directions}

for i, l in enumerate(input):
    if "S" in l:
        x, y = (l.index('S'), i)


sum = 0
loop = mark_loop(x, y)
for y in range(0, len(input)):  
    for x in range(0, len(input[y])):  
        if (x,y) not in loop:
            input[y][x] = '.'

for l in input:
    print(''.join(l))

