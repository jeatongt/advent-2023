# python
import re

max_red = 12
max_blue = 14
max_green = 13

def is_this_game_possible(game_string, max_red, max_blue, max_green):
    game_number = re.match(r'Game (\d+):', game_string).group(1)
    is_impossible = False
    reds_shown = re.findall(r'(\d+) red', game_string)
    blues_shown = re.findall(r'(\d+) blue', game_string)
    greens_shown = re.findall(r'(\d+) green', game_string)
    is_impossible = any(int(red) > max_red for red in reds_shown)
    if is_impossible:
        return 0
    is_impossible = any(int(blue) > max_blue for blue in blues_shown)
    if is_impossible:
        return 0
    is_impossible = any(int(green) > max_green for green in greens_shown)
    if is_impossible:
        return 0
    else:
        return int(game_number)

total = 0
with open('/Users/jeaton/Git/advent-2023/Day02/cube-games.txt', 'r') as file:
    for line in file.readlines():
        game_string = line.strip()  # remove newline characters
        game_is_possible = is_this_game_possible(game_string, max_red, max_blue, max_green)
        total += game_is_possible
print(total)