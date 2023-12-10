import re
import math
from collections import Counter

input = open("input.txt", "r") .readlines()
instructions = re.search(r"\w+", input[0]).group(0)
instructions_len = len(instructions)
p = re.compile(r"\w+")
input = list(map(lambda l: re.findall(p, l), input[2:]))
positions = []
start_positions = []
positions_graph = dict()
for p, l, r in input:
    positions_graph[(p,'L')] = l
    positions_graph[(p,'R')] = r
    positions.append(p)
    if p[-1] == 'A':
        start_positions.append(p)

# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def find_next_z(state):
    position, steps = state
    while True:
        position = positions_graph[position, instructions[steps % instructions_len]]
        steps += 1
        if position[-1] == 'Z':
            return (position, steps)

prefixes = []
for state in [(p, 0) for p in start_positions]:      
    first_z = find_next_z(state)
    second_z = find_next_z(first_z)
    _, pref = first_z
    prefixes.append(pref)
    # turns out loop always in same length
    
print(math.lcm(*prefixes))