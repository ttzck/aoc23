import re

input = open("input.txt", "r")
p = re.compile(r"\d+")
wins = []

for l in input:
    a, b = l.split('|')
    winning = set(re.findall(p, a)[1:])
    my = set(re.findall(p, b))
    wins.append(len(winning & my))

cards = [1 for _ in wins]
for i, card in enumerate(cards):
    for j in range(i+1, i+1+wins[i]):
        cards[j] += card

print(sum(cards))