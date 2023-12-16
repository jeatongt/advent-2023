# python
import re

def get_winning_numbers(card_string):
    winning_numbers = []
    matches = re.findall(r':(.*?)(?=\|)', card_string)
    if matches:
        for match in matches:
            winning_numbers = [int(num) for num in re.findall(r'\d+', match)]
    return winning_numbers

def get_my_numbers(card_string):
    my_numbers = []
    matches = re.findall(r'\|\s*(.*)', card_string)
    if matches:
        for match in matches:
            my_numbers = [int(num) for num in re.findall(r'\d+', match)]
    return my_numbers

def score_of_this_card(card_string):
    print(card_string)
    winning_numbers = get_winning_numbers(card_string)
    print(winning_numbers)
    my_numbers = get_my_numbers(card_string)
    print(my_numbers)
    score = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score

total_score = 0
with open('/Users/jeaton/Git/advent-2023/Day04/test-input.txt', 'r') as file:
    for line in file.readlines():
        total_score += score_of_this_card(line.strip())
print(total_score)