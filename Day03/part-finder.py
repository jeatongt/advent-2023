# python
import re

def symbol_is_in_this_span(schematic_string, start, end):
    if schematic_string is None:
        return False
    if start < 0:
        start = 0
    if end > len(schematic_string):
        end = len(schematic_string)
    if re.search(r'[^\d\.]', schematic_string[start:end]):
        return True

def sum_of_part_numbers_this_line(previous_schematic_string, schematic_string, next_schematic_string):
    parts_this_line = 0
    # print("Current line:" + schematic_string)
    for part_number in re.finditer(r'(\d+)', schematic_string):
        # print(part_number)
        # print(previous_schematic_string)
        # print(schematic_string)
        # print(next_schematic_string)
        if symbol_is_in_this_span(previous_schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
            # print("Matched previous")
        elif symbol_is_in_this_span(schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
            # print("Matched current")
        elif symbol_is_in_this_span(next_schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
            # print("Matched next")
    return parts_this_line

total = 0
previous_line = None
current_line = None
with open('/Users/jeaton/Git/advent-2023/Day03/engine-schematic.txt', 'r') as file:
    for next_line in file.readlines():
        if current_line is not None:
            total += sum_of_part_numbers_this_line(previous_line, current_line, next_line)
        previous_line = current_line
        current_line = next_line.strip()
    next_line = None
    total += sum_of_part_numbers_this_line(previous_line, current_line, next_line)
print(total)