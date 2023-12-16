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
    # print(card_string)
    winning_numbers = get_winning_numbers(card_string)
    # print(winning_numbers)
    my_numbers = get_my_numbers(card_string)
    # print(my_numbers)
    score = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            score += 1
    return score

def get_winning_copies(original_cards, cards_to_score):
    winning_copies = []
    for card in cards_to_score:
        card_id = re.search(r'Card\s*(\d+)').group(1)
        print(card_id)
        for i in range(score_of_this_card(card)):
            winning_copies.append(original_cards[int(card_id)+i+1])
    return winning_copies


def get_count_of_these_cards_and_their_copies(original_cards, cards_to_score):
    card_count = get_count_of_these_cards_and_their_copies(original_cards, get_winning_copies(original_cards, cards_to_score))+len(cards_to_score)
    return card_count

with open('/Users/jeaton/Git/advent-2023/Day04/scratchcards.txt', 'r') as file:
    original_cards = file.readlines()
    total_count = get_count_of_these_cards_and_their_copies(original_cards, original_cards)
    print(total_count)
