# python
import re

def make_map(map_lines):
    map = {}
    for line in map_lines:
        matches = re.findall(r'(\d+)\s*(\d+)\s*(\d+)', line)
        if matches:
            for match in matches:
                for i in range(int(match[2])):
                    map[int(match[1]) + i] = int(match[0]) + i
    return map

def get_map_value(map, key):
    if key in map:
        return map[key]
    else:
        return key

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
            map_name = re.search(r'(.*)\smap:', map_file[i]).group(1)
            map_lines = []
            while i < len(map_file) - 1 and map_file[i+1] != '':
                map_lines.append(map_file[i+1])
                i += 1
            if map_name == 'seed-to-soil':
                seed_soil_map = make_map(map_lines)
                # print(seed_soil_map)
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
seed_location_map = {}
for seed in seeds:
    seed_location_map[seed] = get_map_value(humidity_location_map, get_map_value(temperature_humidity_map, get_map_value(light_temperature_map, get_map_value(water_light_map, get_map_value(fertilizer_water_map, get_map_value(soil_fertilizer_map, get_map_value(seed_soil_map, seed)))))))
print(seed_location_map)