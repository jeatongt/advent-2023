# python

import re

def find_list_of_winning_button_times(time, distance):
    winning_times = []
    for i in range(time):
        if (time - i) * i > distance:
            winning_times.append(i)
    return winning_times

with open('/Users/jeaton/Git/advent-2023/Day06/real-races.txt', 'r') as file:
    race_file_full = file.readlines()
    race_file = [line.strip() for line in race_file_full]
    i = 0
    times = []
    distances = []
    for i in range(len(race_file)):
        if re.search(r'Time:', race_file[i]):
            matches = re.findall(r'Time:\s*(.*)', race_file[i])
            if matches:
                for match in matches:
                    times = [int(num) for num in re.findall(r'\d+', match)]
                    print(times)
        if re.search(r'Distance:', race_file[i]):
            matches = re.findall(r'Distance:\s*(.*)', race_file[i])
            if matches:
                for match in matches:
                    distances = [int(num) for num in re.findall(r'\d+', match)]
                    print(distances)

ways_to_win = []
for i in range(len(times)):
    ways_to_win.append(find_list_of_winning_button_times(times[i], distances[i]))
print(ways_to_win)
permutations_to_win = 1
for i in range(len(ways_to_win)):
    permutations_to_win *= len(ways_to_win[i])
print(permutations_to_win)