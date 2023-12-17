import re

def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= width or y >= height

def energize(x, y, dx, dy):
    beams = [(x, y, dx, dy)]
    seen = set()
    while beams:
        beams_next_step = []
        for (x, y, dx, dy) in beams:
            if out_of_bounds(x, y) or (x, y, dx, dy) in seen: continue
            match input[y][x]:
                case '/':
                    beams_next_step.append((x - dy, y - dx, -dy, -dx))
                case '\\':
                    beams_next_step.append((x + dy, y + dx, dy, dx))
                case '|' if dx != 0:
                    beams_next_step.append((x, y + 1, 0, 1))
                    beams_next_step.append((x, y - 1, 0, -1))
                case '-' if dy != 0:
                    beams_next_step.append((x + 1, y, 1, 0))
                    beams_next_step.append((x - 1, y, -1, 0))
                case _:
                    beams_next_step.append((x + dx, y + dy, dx, dy))

            seen.add((x, y, dx, dy))
        beams = beams_next_step

    return len({(x, y) for (x, y, _, _) in seen})


input = [re.findall(r"[.\/\\\-|]", l) for l in open("input.txt", "r").readlines()]
width, height = len(input[0]), len(input)
energized = []

for x in range(width):
    energized.append(energize(x, 0, 0, 1))
    energized.append(energize(x, height-1, 0, -1))


for y in range(height):
    energized.append(energize(0, y, 1, 0))
    energized.append(energize(width-1, y, -1, 0))

print(max(energized))