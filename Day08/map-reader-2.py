# python
import re

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
with open('/Users/jeaton/Git/advent-2023/Day08/test-map2.txt', 'r') as file:
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

current_nodes = get_starting_nodes(map_nodes)
steps_taken = 0
print(current_nodes)
while am_i_there_yet(current_nodes) == False:
    for turn in turns:
        current_nodes = turn_and_get_new_node(current_nodes, map_nodes, turn)
        print(current_nodes)
        steps_taken += 1
        if am_i_there_yet(current_nodes) == True:
            break
print(steps_taken)