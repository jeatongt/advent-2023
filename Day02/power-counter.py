# python
import re

def power_of_this_game(game_string):
    reds_shown = re.findall(r'(\d+) red', game_string)
    reds_shown_ints = []
    for red in reds_shown:
        reds_shown_ints.append(int(red))
    blues_shown = re.findall(r'(\d+) blue', game_string)
    blues_shown_ints = []
    for blue in blues_shown:
        blues_shown_ints.append(int(blue))
    greens_shown = re.findall(r'(\d+) green', game_string)
    greens_shown_ints = []
    for green in greens_shown:
        greens_shown_ints.append(int(green))
    power = int(max(reds_shown_ints)) * int(max(blues_shown_ints)) * int(max(greens_shown_ints))
    return power

total = 0
with open('/Users/jeaton/Git/advent-2023/Day02/cube-games.txt', 'r') as file:
    for line in file.readlines():
        game_string = line.strip()  # remove newline characters
        game_string_power = power_of_this_game(game_string)
        total += game_string_power
print(total)