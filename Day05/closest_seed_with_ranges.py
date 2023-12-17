# python
import re
import operator

# seeds: 79 14 55 13
# seed-to-soil map:
# 50 98 2
# 52 50 48
# This function needs to accept a range instead of a key, and return a list of ranges
def get_map_value(map_lines, key):
    for line in map_lines:
        matches = re.findall(r'(\d+)\s*(\d+)\s*(\d+)', line)
        if matches:
            for match in matches:
                if int(match[1]) <= int(key) <= int(match[1]) + int(match[2]) - 1:
                    return int(match[0]) + int(key) - int(match[1])
    return key

def get_best_location(start, seed_range):
    best_seed = None
    best_location = None
    for i in range(int(seed_range)):
        location = get_map_value(humidity_location_map, get_map_value(temperature_humidity_map, get_map_value(light_temperature_map, get_map_value(water_light_map, get_map_value(fertilizer_water_map, get_map_value(soil_fertilizer_map, get_map_value(seed_soil_map, int(start) + i)))))))
        if best_location is None or location < best_location:
            best_seed = int(start) + i
            best_location = location
    return best_seed, best_location

with open('/Users/jeaton/Git/advent-2023/Day05/test-map.txt', 'r') as file:
    map_file_full = file.readlines()
    map_file = [line.strip() for line in map_file_full]
    i = 0
    seeds = {}
    for i in range(len(map_file)):
        if re.search(r'seeds:', map_file[i]):
            matches = re.findall(r'(\d+)\s*(\d+)', map_file[i])
            if matches:
                for match in matches:
                    seeds[match[0]] = match[1]
        if re.search(r'map:', map_file[i]):
            map_name = re.search(r'(.*)\smap:', map_file[i]).group(1)
            map_lines = []
            while i < len(map_file) - 1 and map_file[i+1] != '':
                map_lines.append(map_file[i+1])
                i += 1
            if map_name == 'seed-to-soil':
                seed_soil_map = map_lines
            if map_name == 'soil-to-fertilizer':
                soil_fertilizer_map = map_lines
            if map_name == 'fertilizer-to-water':
                fertilizer_water_map = map_lines
            if map_name == 'water-to-light':
                water_light_map = map_lines
            if map_name == 'light-to-temperature':
                light_temperature_map = map_lines
            if map_name == 'temperature-to-humidity':
                temperature_humidity_map = map_lines
            if map_name == 'humidity-to-location':
                humidity_location_map = map_lines
seed_location_map = {}
print(seeds)
for key, value in seeds.items():
    location_map_seed, location_map_location = get_best_location(key, value)
    print("Best location for seed range " + key + " is " + str(location_map_seed) + " at " + str(location_map_location))
    seed_location_map[location_map_seed] = location_map_location
sorted_seed_location_map = dict(sorted(seed_location_map.items(), key=operator.itemgetter(1)))
first_key, first_value = next(iter(sorted_seed_location_map.items()))
print(f"Seed: {first_key}, Location: {first_value}")