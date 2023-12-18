# python

import re

def find_list_of_winning_button_times(time, distance):
    winning_times = []
    for i in range(time):
        if (time - i) * i > distance:
            winning_times.append(i)
    return winning_times

with open('/Users/jeaton/Git/advent-2023/Day06/test-races.txt', 'r') as file:
    race_file_full = file.readlines()
    race_file = [line.strip() for line in race_file_full]
    i = 0
    for i in range(len(race_file)):
        if re.search(r'Time:', race_file[i]):
            matches = re.findall(r'(\d+)', race_file[i])
            if matches:
                times = ''.join(matches)
                print(times)
        if re.search(r'Distance:', race_file[i]):
            matches = re.findall(r'(\d+)', race_file[i])
            if matches:
                distances = ''.join(matches)
                print(distances)

ways_to_win = find_list_of_winning_button_times(int(times), int(distances))
# print(ways_to_win)
permutations_to_win = len(ways_to_win)
print(permutations_to_win)