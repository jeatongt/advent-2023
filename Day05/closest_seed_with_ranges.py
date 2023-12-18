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
# Humidity map:
# {78: 3, 82: 4, 90: 9, 46: 11}
# Humidity-location map:
# ['60 56 37', '56 93 4']
# Start 78 is in range 56 to 92
# Start 82 is in range 56 to 92
# Start 90 is in range 56 to 92
# No matches - passing through 46: 11
# Location map:
# {82: 3, 86: 4, 94: 9, 46: 11}
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
                    if int(match[1]) <= key <= (int(match[1]) + int(match[2]) - 1):
                        print('Start ' + str(key) + ' is in range ' + str(match[1]) + ' to ' + str(int(match[1]) + int(match[2]) - 1))
                        if key + value <= int(match[1]) + int(match[2]):
                            dest_temp_dict[key + int(match[0]) - int(match[1])] = value
                        else:
                            start_diff = int(match[0]) - int(match[1])
                            range_diff = key + value - int(match[1]) - int(match[2])
                            dest_temp_dict[key + start_diff] = value - range_diff
                            additional_ranges_dict[key + value - range_diff] = range_diff
        if dest_temp_dict:
            destination_dict.update(dest_temp_dict)
        else:
            print('No matches - passing through ' + str(key) + ': ' + str(value))
            destination_dict[key] = value
    if additional_ranges_dict:
        print('Need moar ranges!')
        destination_dict.update(get_map_ranges(map_lines, additional_ranges_dict))
    return destination_dict

with open('/Users/jeaton/Git/advent-2023/Day05/full-map.txt', 'r') as file:
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

print('Seeds:')
print(seeds)
print('Seed-soil map:')
print(seed_soil_map)
soil_map = get_map_ranges(seed_soil_map, seeds)
print('Soil map:')
print(soil_map)
print('Soil-fertilizer map:')
print(soil_fertilizer_map)
fertilizer_map = get_map_ranges(soil_fertilizer_map, soil_map)
print('Fertilizer map:')
print(fertilizer_map)
print('Fertilizer-water map:')
print(fertilizer_water_map)
water_map = get_map_ranges(fertilizer_water_map, fertilizer_map)
print('Water map:')
print(water_map)
print('Water-light map:')
print(water_light_map)
light_map = get_map_ranges(water_light_map, water_map)
print('Light map:')
print(light_map)
print('Light-temperature map:')
print(light_temperature_map)
temperature_map = get_map_ranges(light_temperature_map, light_map)
print('Temperature map:')
print(temperature_map)
print('Temperature-humidity map:')
print(temperature_humidity_map)
humidity_map = get_map_ranges(temperature_humidity_map, temperature_map)
print('Humidity map:')
print(humidity_map)
print('Humidity-location map:')
print(humidity_location_map)
location_map = get_map_ranges(humidity_location_map, humidity_map)
print('Location map:')
print(location_map)
print('Best location is ' + str(min(location_map)))