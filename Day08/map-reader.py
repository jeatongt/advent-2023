# python
import re

map_lines = []
with open('/Users/jeaton/Git/advent-2023/Day08/full-map.txt', 'r') as file:
    for line in file.readlines():
        map_lines.append(line.strip())
    turns = list(map_lines[0])
    map_nodes = {}
    for i in range(2, len(map_lines)):
        matches = re.findall(r'([A-Z]+)', map_lines[i])
        if matches:
            map_nodes[matches[0]] = [matches[1], matches[2]]
print(turns)
print(map_nodes)

current_node = 'AAA'
steps_taken = 0
print(current_node)
while current_node != 'ZZZ':
    for turn in turns:
        if turn == 'L':
            current_node = map_nodes[current_node][0]
            print(current_node)
            steps_taken += 1
            if current_node == 'ZZZ':
                break
        if turn == 'R':
            current_node = map_nodes[current_node][1]
            print(current_node)
            steps_taken += 1
            if current_node == 'ZZZ':
                break
print(steps_taken)