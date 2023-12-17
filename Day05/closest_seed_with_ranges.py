# python
import re
import operator

# seeds: 79 14 55 13
# seed-to-soil map:
# 50 98 2
# 52 50 48
# get_map_ranges(["50 98 2", "52 50 48"], {'79': '20', '55': '13'}) 
#     -> {'81': '19', '57': '13', '50': '1'}
#     -> {'79+52-50': '20-(79+20-50-48)', '57': '13', get_map_ranges(["50 98 2", "52 50 48"], {'98': '1'})
# This function needs to accept a dict of ranges instead of a key, and return a dict of ranges
def get_map_ranges(map_lines, source_dict):
    destination_dict = {}
    additional_ranges_dict = {}
    for key, value in source_dict.items():
        dest_temp_dict = {}
        for line in map_lines:
            matches = re.findall(r'(\d+)\s*(\d+)\s*(\d+)', line)
            if matches:
                for match in matches:
                    if int(match[1]) <= key <= int(match[1]) + int(match[2]) - 1:
                        if value <= int(match[2]):
                            dest_temp_dict[key + int(match[0]) - int(match[1])] = value
                        else:
                            start_diff = int(match[0]) - int(match[1])
                            range_diff = key + value - int(match[1]) - int(match[2])
                            dest_temp_dict[key + start_diff] = value - range_diff
                            additional_ranges_dict[key + value - range_diff] = range_diff
        if dest_temp_dict:
            destination_dict.update(dest_temp_dict)
        else:
            destination_dict[key] = value
    if additional_ranges_dict:
        destination_dict.update(get_map_ranges(map_lines, additional_ranges_dict))
    return destination_dict

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
                    seeds[int(match[0])] = int(match[1])
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
print(seeds)
soil_map = get_map_ranges(seed_soil_map, seeds)
print(soil_map)
fertilizer_map = get_map_ranges(soil_fertilizer_map, soil_map)
print(fertilizer_map)
water_map = get_map_ranges(fertilizer_water_map, fertilizer_map)
print(water_map)
light_map = get_map_ranges(water_light_map, water_map)
print(light_map)
temperature_map = get_map_ranges(light_temperature_map, light_map)
print(temperature_map)
humidity_map = get_map_ranges(temperature_humidity_map, temperature_map)
print(humidity_map)
location_map = get_map_ranges(humidity_location_map, humidity_map)
print(location_map)
print('Best location is ' + str(min(location_map)))