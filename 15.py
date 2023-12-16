import re


def hashf(string):
    curr = 0
    for c in string:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


input = re.findall(r'(\w+)([=-])(\d*)', open("input.txt", "r").read())

boxes = [[] for _ in range(256)]
for label, symbol, value in input:
    hash = hashf(label)
    match symbol:
        case '=':
            for lv in boxes[hash]:
                if lv[0] == label:
                    lv[1] = value
                    break
            else:
                    boxes[hash].append([label, value])
        case '-':
            for lv in boxes[hash]:
                if lv[0] == label:
                    boxes[hash].remove(lv)
                    break
print(sum([i * j * int(focal_length) for i, box in enumerate(boxes, 1) for j, [_, focal_length] in enumerate(box, 1)]))
