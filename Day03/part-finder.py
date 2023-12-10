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
    for part_number in re.finditer(r'(\d+)', schematic_string):
        if symbol_is_in_this_span(previous_schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
        elif symbol_is_in_this_span(schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
        elif symbol_is_in_this_span(next_schematic_string, part_number.start()-1, part_number.end()+1):
            parts_this_line += int(part_number.group(1))
    return parts_this_line

