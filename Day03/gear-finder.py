# python
import re

def find_gears_in_this_span(schematic_string, start, end, line_number, part_number):
    if schematic_string is None:
        return None
    if start < 0:
        start = 0
    if end > len(schematic_string):
        end = len(schematic_string)
    gears_this_part = {}
    for gear in re.finditer(r'\*', schematic_string[start:end]):
        key = str(line_number) + ',' + str(gear.start()+start)
        if key not in gears_this_part:
            gears_this_part[key] = []
        gears_this_part[key].append(part_number)
    return gears_this_part

def find_gears_for_parts_in_this_line(previous_schematic_string, schematic_string, next_schematic_string, line_number):
    # print("Current line:" + schematic_string)
    gears_for_parts_in_this_line = {}
    for part_number in re.finditer(r'(\d+)', schematic_string):
        # print(part_number)
        # print(previous_schematic_string)
        # print(schematic_string)
        # print(next_schematic_string)
        gears_previous_line = find_gears_in_this_span(previous_schematic_string, part_number.start()-1, part_number.end()+1, line_number-1, part_number.group())
        if gears_previous_line:
            print(gears_previous_line)
            for key in gears_previous_line:
                if key not in gears_for_parts_in_this_line:
                    gears_for_parts_in_this_line[key] = []
                gears_for_parts_in_this_line[key].extend(gears_previous_line[key])
        gears_this_line = find_gears_in_this_span(schematic_string, part_number.start()-1, part_number.end()+1, line_number, part_number.group())
        if gears_this_line:
            print(gears_this_line)
            for key in gears_this_line:
                if key not in gears_for_parts_in_this_line:
                    gears_for_parts_in_this_line[key] = []
                gears_for_parts_in_this_line[key].extend(gears_this_line[key])
        gears_next_line = find_gears_in_this_span(next_schematic_string, part_number.start()-1, part_number.end()+1, line_number+1, part_number.group())
        if gears_next_line:
            print(gears_next_line)
            for key in gears_next_line:
                if key not in gears_for_parts_in_this_line:
                    gears_for_parts_in_this_line[key] = []
                gears_for_parts_in_this_line[key].extend(gears_next_line[key])
    return gears_for_parts_in_this_line

total = 0
gear_dict = {}
previous_line = None
current_line = None
line_number = 0
with open('/Users/jeaton/Git/advent-2023/Day03/test-input.txt', 'r') as file:
    for next_line in file.readlines():
        next_line = next_line.strip()
        if current_line is not None:
            parts_in_this_line = find_gears_for_parts_in_this_line(previous_line, current_line, next_line, line_number)
            if parts_in_this_line:
                for key in parts_in_this_line:
                        if key not in gear_dict:
                            gear_dict[key] = []
                        gear_dict[key].extend(parts_in_this_line[key])            
            line_number += 1
        previous_line = current_line
        current_line = next_line
    next_line = None
    parts_in_this_line = find_gears_for_parts_in_this_line(previous_line, current_line, next_line, line_number)
    if parts_in_this_line:
        for key in parts_in_this_line:
                if key not in gear_dict:
                    gear_dict[key] = []
                gear_dict[key].extend(parts_in_this_line[key])            
print(gear_dict)