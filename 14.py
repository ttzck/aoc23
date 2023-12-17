import re

def roll_1d(rocks1d, cubes1d):
    rocks1d, cubes1d = sorted(rocks1d), sorted(cubes1d)
    new_rocks = []
    cubes_index, free = 0, 0

    for rock in rocks1d:
        while cubes_index < len(cubes1d) and cubes1d[cubes_index] < rock:
            free = cubes1d[cubes_index] + 1
            cubes_index += 1
        new_rocks.append(free)
        free += 1

    return new_rocks


def score():
    return sum([height - y for (x, y) in rocks])


def show():
    print(f'number of rock: {len(rocks)}')
    for y in range(height):
        l = ''
        for x in range(width):
            if (x, y) in rocks:
                l += 'O'
            elif (x, y) in cubes:
                l += '#'
            else:
                l += '.'
        print(l)
    print()


def group_by_x(things):
    groups = [[] for _ in range(width)]
    for (x, y) in things:
        groups[x].append(y)
    return groups


def group_by_y(things):
    return group_by_x([(y, x) for (x, y) in things])


def roll_north():
    return [(x, y) 
            for x, (rocks_1d, cubes_1d) in enumerate(zip(group_by_x(rocks), group_by_x(cubes))) 
            for y in roll_1d(rocks_1d, cubes_1d)]


def roll_west():
    return [(x, y) 
            for y, (rocks_1d, cubes_1d) in enumerate(zip(group_by_y(rocks), group_by_y(cubes))) 
            for x in roll_1d(rocks_1d, cubes_1d)]


def roll_east():
    return [(x, y) 
            for y, (rocks_1d, cubes_1d) in enumerate(zip(group_by_y(rocks), group_by_y(cubes))) 
            for x in mirror_vertical(roll_1d(mirror_vertical(rocks_1d), mirror_vertical(cubes_1d)))]


def roll_south():
    return [(x, y) 
            for x, (rocks_1d, cubes_1d) in enumerate(zip(group_by_x(rocks), group_by_x(cubes))) 
            for y in mirror_horizontal(roll_1d(mirror_horizontal(rocks_1d), mirror_horizontal(cubes_1d)))]


def mirror_vertical(things):
    return [width - t - 1 for t in things]


def mirror_horizontal(things):
    return [height - t - 1 for t in things]


input = [l.strip() for l in open("input.txt", "r").readlines()]
cycles = 1000000000
width, height = len(input[0]), len(input)
rocks = [(x, y) for y, l in enumerate(input) for x, c in enumerate(l) if c == 'O']
cubes = [(x, y) for y, l in enumerate(input) for x, c in enumerate(l) if c == '#']
#print(rocks)
#print(cubes)
for cycle in range(500):
    rocks = roll_north()
    rocks = roll_west()
    rocks = roll_south()
    rocks = roll_east()
    print(f"{cycle + 1} -> {score()}")