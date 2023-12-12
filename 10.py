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


def out_of_bounds(x, y):
    return x < 0 or x >= len(input[0]) or y < 0 or y >= len(input)


def write_at(x, y, c):
    if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input):
        return
    input[y][x] = c

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


def get_path(x, y):
    path = []
    last_step = None
    while True:
        p = pipe_at(x, y)
        for d in allowed_directions[p]:
            if last_step != None and d == opposite(last_step):
                continue
            dx, dy = translations[d]
            if pipe_at(x + dx, y + dy) in allowed_pipes[opposite(d)]:
                x, y = x + dx, y + dy
                path.append(d)
                last_step = d
                if pipe_at(x, y) == 'S': return path
                else: break


def write_path(x, y, path):
    while path:
        d = path.pop(0)
        write_at(x, y, d)
        dx, dy = translations[d]
        x, y = x + dx, y + dy


def flood_path(x, y, path):
    while path:
        d = path.pop(0)
        match d:
            case 'n':
                flood_fill(x + 1, y, 'I')
                flood_fill(x + 1, y - 1, 'I')
                flood_fill(x - 1, y, 'O')
            case 'e':
                flood_fill(x, y + 1, 'I')
                flood_fill(x + 1, y + 1, 'I')
                flood_fill(x, y - 1, 'O')
            case 's':
                flood_fill(x - 1, y, 'I')
                flood_fill(x - 1, y + 1, 'I')
                flood_fill(x + 1, y, 'O')
            case 'w':
                flood_fill(x, y - 1, 'I')
                flood_fill(x - 1, y - 1, 'I')
                flood_fill(x, y + 1, 'O')
        dx, dy = translations[d]
        x, y = x + dx, y + dy


def flood_fill(x, y, c):
    q = [(x,y)]
    while q:
        x, y = q.pop()
        if out_of_bounds(x,y): continue
        if pipe_at(x,y) not in directions + [c]:
            write_at(x, y, c)
            for d in directions:
                dx, dy = translations[d]
                q.append((x + dx, y + dy))


input = [list(l[:-1]) for l in open("input.txt", "r").readlines()]

directions = ['n', 'e', 's', 'w']
pipes = ['S', '|', '-', 'L', 'J', '7', 'F']

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
path = get_path(x, y)
path2 = copy.deepcopy(path)
write_path(x, y, path)
flood_path(x,y,path2)

sum_i = 0
sum_o = 0

for l in input:
    sum_i += l.count('I')
    sum_o += l.count('O')
    print(''.join(l))

print(sum_i, sum_o)