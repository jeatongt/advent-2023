# python

import re
from collections import Counter

def score_of_this_hand(hand):
    if five_of_a_kind(hand):
        score = 'a'
    elif four_of_a_kind(hand):
        score = 'b'
    elif full_house(hand):
        score = 'c'
    elif three_of_a_kind(hand):
        score = 'd'
    elif two_pair(hand):
        score = 'e'
    elif one_pair(hand):
        score = 'f'
    else:
        score = 'g'
    score += high_cards(hand)
    return score

def five_of_a_kind(hand):
    same_card = Counter(hand)

    

hands = []
with open('/Users/jeaton/Git/advent-2023/Day07/test-hands.txt', 'r') as file:
    for line in file.readlines():
        this_hand = []
        cards = re.findall(r'\w+', line.strip())
        if cards:
            this_hand = list(cards[0])
            this_hand.append(cards[1])
        hands.append(this_hand)
print(hands)
    
