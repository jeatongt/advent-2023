# python
import re

def find_gears_in_this_span(schematic_string, start, end, line_number, part_number):
    if schematic_string is None:
        return None
    if start < 0:
        start = 0
    if end > len(schematic_string):
        end = len(schematic_string)
    gears_this_part = []
    for gear in re.finditer(r'\*', schematic_string[start:end]):
        this_gear = {'gear_line': line_number, 'gear_position': gear.start()+start, 'part_number': part_number}
        print(this_gear)
        gears_this_part.append(this_gear)
    return gears_this_part

def find_gears_for_parts_in_this_line(previous_schematic_string, schematic_string, next_schematic_string, line_number):
    # print("Current line:" + schematic_string)
    gears_for_parts_in_this_line = []
    for part_number in re.finditer(r'(\d+)', schematic_string):
        # print(part_number)
        # print(previous_schematic_string)
        # print(schematic_string)
        # print(next_schematic_string)
        gears_previous_line = find_gears_in_this_span(previous_schematic_string, part_number.start()-1, part_number.end()+1, line_number-1, part_number.group())
        if gears_previous_line:
            gears_for_parts_in_this_line.append(gears_previous_line)
        gears_this_line = find_gears_in_this_span(schematic_string, part_number.start()-1, part_number.end()+1, line_number, part_number.group())
        if gears_this_line:
            gears_for_parts_in_this_line.append(gears_this_line)
        gears_next_line = find_gears_in_this_span(next_schematic_string, part_number.start()-1, part_number.end()+1, line_number+1, part_number.group())
        if gears_next_line:
            gears_for_parts_in_this_line.append(gears_next_line)
    return gears_for_parts_in_this_line

total = 0
gear_dict = []
previous_line = None
current_line = None
line_number = 0
with open('/Users/jeaton/Git/advent-2023/Day03/test-input.txt', 'r') as file:
    for next_line in file.readlines():
        next_line = next_line.strip()
        if current_line is not None:
            parts_in_this_line = find_gears_for_parts_in_this_line(previous_line, current_line, next_line, line_number)
            if parts_in_this_line:
                gear_dict.append(parts_in_this_line)
            line_number += 1
        previous_line = current_line
        current_line = next_line
    next_line = None
    parts_in_this_line = find_gears_for_parts_in_this_line(previous_line, current_line, next_line, line_number)
    if parts_in_this_line:
        gear_dict.append(parts_in_this_line)
print(gear_dict)