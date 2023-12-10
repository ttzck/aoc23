import re
from collections import Counter

input = open("input.txt", "r") .readlines()
cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
joker = cards.index('J')
p = re.compile(r"(\w+)\s(\d+)")
input = map(lambda l: re.match(p, l).groups(), input)
input = [
    ([cards.index(c) for c in h], int(b)) 
    for (h, b) in input
]
hands = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]


def add_hand_type(l):
    hand, bid = l

    if hand == [joker] * 5:
        return ([0] + hand, bid)

    jokers = hand.count(joker)
    no_jokers = [c for c in hand if c is not joker] 
    freq = sorted(Counter(no_jokers).values())
    freq[-1] += jokers
    type = hands.index(freq)
    return ([type] + hand, bid)

order = (sorted(map(add_hand_type, input), reverse=True))
sum = 0
for i, (h, b) in enumerate(order):
    sum += (i + 1) * b
print(sum)