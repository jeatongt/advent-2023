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
        card_id = re.search(r'Card\s*(\d+)', card).group(1)
        card_score = score_of_this_card(card)
        # print('Card ' + card_id + ' scored ' + str(card_score))
        if card_score > 0:
            for i in range(score_of_this_card(card)):
                winning_copies.append(original_cards[int(card_id)+i].strip())
    return winning_copies


def get_count_of_these_cards_and_their_copies(original_cards, cards_to_score):
    winning_copies = get_winning_copies(original_cards, cards_to_score)
    if winning_copies:
        # print(str(len(winning_copies)) + ' winning copies')
        # print(winning_copies)
        return get_count_of_these_cards_and_their_copies(original_cards, winning_copies) + len(cards_to_score)
    else:
        return len(cards_to_score)

with open('/Users/jeaton/Git/advent-2023/Day04/scratchcards.txt', 'r') as file:
    original_cards = file.readlines()
    total_count = get_count_of_these_cards_and_their_copies(original_cards, original_cards)
    print(total_count)
