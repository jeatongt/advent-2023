# python

import re

hands = []
with open('/Users/jeaton/Git/advent-2023/Day07/test-hands.txt', 'r') as file:
    for line in file.readlines():
        this_hand = []
        print(line)
        cards = re.search(r'([^ ]*)', line)
        print(cards)
    
