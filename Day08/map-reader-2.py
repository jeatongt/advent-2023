# python
import re
import math
from functools import reduce

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

def turn_and_get_new_node(current_nodes, map_nodes, direction):
    turnt_nodes = []
    for node in current_nodes:
        if direction == 'L':
            turnt_nodes.append(map_nodes[node][0])
        if direction == 'R':
            turnt_nodes.append(map_nodes[node][1])
    return turnt_nodes

def am_i_there_yet(current_nodes):
    for node in current_nodes:
        if node[2] != 'Z':
            return False
    return True

def get_starting_nodes(map_nodes):
    starting_nodes = []
    for node in map_nodes:
        if node[2] == 'A':
            starting_nodes.append(node)
    return starting_nodes

map_lines = []
with open('/Users/jeaton/Git/advent-2023/Day08/full-map.txt', 'r') as file:
    for line in file.readlines():
        map_lines.append(line.strip())
    turns = list(map_lines[0])
    map_nodes = {}
    for i in range(2, len(map_lines)):
        matches = re.findall(r'([0-9|A-Z]+)', map_lines[i])
        if matches:
            map_nodes[matches[0]] = [matches[1], matches[2]]
print(turns)
print(map_nodes)

starting_nodes = get_starting_nodes(map_nodes)
steps_taken = 0
steps_list = []
print(starting_nodes)
for node in starting_nodes:
    current_node = node
    steps_taken = 0
    print(node)
    while current_node[2] != 'Z':
        for turn in turns:
            if turn == 'L':
                current_node = map_nodes[current_node][0]
                # print(current_node)
                steps_taken += 1
                if current_node[2] == 'Z':
                    break
            if turn == 'R':
                current_node = map_nodes[current_node][1]
                # print(current_node)
                steps_taken += 1
                if current_node[2] == 'Z':
                    break
    print(steps_taken)
    steps_list.append(steps_taken)
print(lcm_list(steps_list))