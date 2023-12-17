# python
import re

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