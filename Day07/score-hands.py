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
    for rank in same_card:
        if same_card[rank] == 5:
            return True
    return False

def four_of_a_kind(hand):
    same_card = Counter(hand)
    for rank in same_card:
        if same_card[rank] == 4:
            return True
    return False

def full_house(hand):
    same_card = Counter(hand)
    if len(same_card) == 2:
        return True
    return False

def three_of_a_kind(hand):
    same_card = Counter(hand)
    for rank in same_card:
        if same_card[rank] == 3:
            return True
    return False

def two_pair(hand):
    same_card = Counter(hand)
    if len(same_card) == 3:
        return True
    return False

def one_pair(hand):
    same_card = Counter(hand)
    if len(same_card) == 4:
        return True
    return False

def high_cards(hand):
    card_values = ''
    rank_values = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'}
    for card in hand:
        card_values += rank_values[card]
    return card_values    

hands = []
with open('/Users/jeaton/Git/advent-2023/Day07/full-hands.txt', 'r') as file:
    for line in file.readlines():
        this_hand = []
        cards = re.findall(r'\w+', line.strip())
        if cards:
            this_hand = list(cards[0])
            this_hand.append(cards[1])
            this_hand.append(score_of_this_hand(this_hand[:5]))
        hands.append(this_hand)
print(hands)
sorted_hands = sorted(hands, key=lambda x: x[6], reverse=True)
winnings = 0
for i in range(len(sorted_hands)):
    place = i + 1
    winnings += int(sorted_hands[i][5])*place
print(winnings)
    
