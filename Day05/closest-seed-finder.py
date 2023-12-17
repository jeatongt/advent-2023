# python
import re

def make_map(map_lines):
    map = {}
    for line in map_lines:
        matches = re.findall(r'(\d+)\s*(\d+)\s*(\d+)', line)
        if matches:
            for i in range(matches[2]):
                map[int(matches[1]) + i] = int(matches[0]) + i
    return map

with open('/Users/jeaton/Git/advent-2023/Day05/test-map.txt', 'r') as file:
    map_file_full = file.readlines()
    map_file = [line.strip() for line in map_file_full]
    i = 0
    seeds = []
    for i in range(len(map_file)):
        if re.search(r'seeds:', map_file[i]):
            matches = re.findall(r'seeds:\s*(.*)', map_file[i])
            if matches:
                for match in matches:
                    seeds = [int(num) for num in re.findall(r'\d+', match)]
                    print(seeds)
        if re.search(r'map:', map_file[i]):
            map_name = re.search(r'(.*)\smap:)', map_file[i]).group(1)
            map_lines = []
            while map_file[i+1] != '':
                map_lines.append(map_file[i+1])
                i += 1
            if map_name == 'seed-to-soil':
                seed_soil_map = make_map(map_lines)
                print(seed_soil_map)
            if map_name == 'soil-to-fertilizer':
                soil_fertilizer_map = make_map(map_lines)
            if map_name == 'fertilizer-to-water':
                fertilizer_water_map = make_map(map_lines)
            if map_name == 'water-to-light':
                water_light_map = make_map(map_lines)
            if map_name == 'light-to-temperature':
                light_temperature_map = make_map(map_lines)
            if map_name == 'temperature-to-humidity':
                temperature_humidity_map = make_map(map_lines)
            if map_name == 'humidity-to-location':
                humidity_location_map = make_map(map_lines)