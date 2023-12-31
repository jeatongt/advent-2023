# python

import re
from collections import Counter

def score_of_this_hand(hand):
    jokers_hand = list(hand)
    jokers_hand = jokers_wild(jokers_hand)
    if five_of_a_kind(jokers_hand):
        score = 'a'
    elif four_of_a_kind(jokers_hand):
        score = 'b'
    elif full_house(jokers_hand):
        score = 'c'
    elif three_of_a_kind(jokers_hand):
        score = 'd'
    elif two_pair(jokers_hand):
        score = 'e'
    elif one_pair(jokers_hand):
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
    rank_values = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'm', 'T': 'd', '9': 'e', '8': 'f', '7': 'g', '6': 'h', '5': 'i', '4': 'j', '3': 'k', '2': 'l'}
    for card in hand:
        card_values += rank_values[card]
    return card_values    

# ['6', 'T', 'K', 'J', 'T', '701', 'eiebde']
def jokers_wild(joker_conversion):
    if 'J' not in joker_conversion:
        return joker_conversion
    same_card = Counter(joker_conversion)
    sorted_same_card = dict(sorted(same_card.items(), key=lambda item: item[1], reverse=True))
    for rank in sorted_same_card:
        if sorted_same_card[rank] == 5:
            return joker_conversion
        if rank != 'J':
            joker_conversion = [rank if x == 'J' else x for x in joker_conversion]
            break
    return joker_conversion

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
sorted_hands = sorted(hands, key=lambda x: x[6], reverse=True)
winnings = 0
print(sorted_hands)
for i in range(len(sorted_hands)):
    place = i + 1
    winnings += int(sorted_hands[i][5])*place
print(winnings)
    
