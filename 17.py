import re
import math
import queue

def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= width or y >= height


def opposite(dir):
    if dir == None: return None
    x, y = dir 
    return (-x, - y)

MAX_STEPS = 3

def dijkstra():
    dist = [[[math.inf for _ in range(MAX_STEPS + 1)] for _ in l] for l in input]
    prev = [[[None for _ in range(MAX_STEPS + 1)] for _ in l] for l in input]
    dir = [[[None for _ in range(MAX_STEPS + 1)] for _ in l] for l in input]

    q = queue.PriorityQueue()
    dist[0][0][0] = 0
    q.put((0, (0, 0, 0)))

    while not q.empty():
        (p, (x, y, i)) = q.get()
        if dist[y][x][i] < p: continue
        for (dx, dy) in directions:
            
            if (dx, dy) == opposite(dir[y][x][i]): continue
            if (dx, dy) == dir[y][x][i] and i > MAX_STEPS: continue
            if out_of_bounds(x + dx, y + dy): continue

            j = i + 1 if (dx, dy) == dir[y][x][i] else 1

            alt = dist[y][x][i] + input[y + dy][x + dx]
            if alt < dist[y + dy][x + dx][j]:
                dist[y + dy][x + dx][j] = alt
                prev[y + dy][x + dx][j] = (x, y, i)
                dir[y + dy][x + dx][j] = (dx, dy)
                q.put((alt, (x + dx, y + dy, j)))
    
    return dist, prev, dir


input = [[int(d) for d in re.findall(r"\d", l)] for l in open("input.txt", "r").readlines()]
width, height = len(input[0]), len(input)
directions = [(1,0), (0,1), (-1,0), (0,-1)]
dist, prev, dir = dijkstra()
print(dist[-1][-1])