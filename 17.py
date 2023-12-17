import re
import math
import queue

def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= width or y >= height


def opposite(dir):
    if dir == None: return (0,0)
    x, y = dir 
    return (-x, - y)

MIN_STEPS = 4
MAX_STEPS = 10

def dijkstra():
    dist = {(x, y, i, dir) : math.inf for x in range(width) for y in range(height) for i in range(MAX_STEPS + 1) for dir in directions}
    prev = {(x, y, i, dir) : None for x in range(width) for y in range(height) for i in range(MAX_STEPS + 1) for dir in directions}

    q = queue.PriorityQueue()
    dist[(0, 0, 0, None)] = 0
    q.put((0, (0, 0, 0, None)))

    while not q.empty():
        (p, (x, y, i, dir)) = q.get()
        if dist[(x, y, i, dir)] < p: continue
        for (dx, dy) in directions:
            
            if (dx, dy) == opposite(dir): continue
            if ((dx, dy) != dir and i < MIN_STEPS) and dir != None: continue
            if (dx, dy) == dir and i >= MAX_STEPS: continue
            if out_of_bounds(x + dx, y + dy): continue

            j = i + 1 if (dx, dy) == dir else 1

            alt = dist[(x, y, i, dir)] + input[y + dy][x + dx]
            if alt < dist[(x + dx, y + dy, j, (dx, dy))]:
                dist[(x + dx, y + dy, j, (dx, dy))] = alt
                prev[(x + dx, y + dy, j, (dx, dy))] = (x, y, i, dir)
                q.put((alt, (x + dx, y + dy, j, (dx, dy))))
    
    return dist, prev, dir


input = [[int(d) for d in re.findall(r"\d", l)] for l in open("input.txt", "r").readlines()]
width, height = len(input[0]), len(input)
directions = [(1,0), (0,1), (-1,0), (0,-1)]
dist, prev, dir = dijkstra()
print(min([dist[width-1, height-1, i, dir] for i in range(MAX_STEPS+1) for dir in directions]))