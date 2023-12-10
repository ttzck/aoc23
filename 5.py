import re

input = open("input.txt", "r")
p1 = re.compile(r"(\d+)\s(\d+)")
p2 = re.compile(r"(\d+)\s(\d+)\s(\d+)")

input = input.read().split('\n\n')
keys = [(int(k), int(r)) for (k, r) in re.findall(p1, input[0])]
tables = [[(int(dst), int(src), int(r)) for (dst, src, r) in re.findall(p2, table)] 
      for table in input[1:]]


print(keys)
for table in tables:
    mapped = []
    for dst, src, src_r in table:
        unmapped = []
        for key, key_r in keys:
            right_most_left = max(key, src)
            left_most_right = min(key + key_r, src + src_r)

            if right_most_left < left_most_right:
                mapped.append((dst + right_most_left - src, left_most_right - right_most_left))

            if key < src:
                if key + key_r <= src:
                    unmapped.append((key, key_r))
                else:
                    unmapped.append((key, src - key))
            if key + key_r > src + src_r:
                if key >= src + src_r:
                    unmapped.append((key, key_r))
                else:
                    unmapped.append((src + src_r, key + key_r - (src + src_r)))
            keys = unmapped
    keys = unmapped + mapped
    print(keys)
                

print(min(keys)[0])
