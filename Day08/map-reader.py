# python
import re

map_lines = []
with open('/Users/jeaton/Git/advent-2023/Day08/test-map.txt', 'r') as file:
    for line in file.readlines():
        map_lines.append(line.strip())
    print(map_lines)
    turns = list(map_lines[0])
    map_nodes = {}
    for i in range(2, len(map_lines)):
        matches = re.findall(r'[A-Z]+', map_lines[i])
        if matches:
            for match in matches:
                map_nodes[match[0]] = [match[1], match[2]]
print(turns)
print(map_nodes)
        