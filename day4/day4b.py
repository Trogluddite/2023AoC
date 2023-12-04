#!/usr/bin/env python3
from copy import copy 

# build a 2d array of functions, each returns the character in the x,y position
def getCards():
    cards = {}
    for idx, row in enumerate(open('input.txt').readlines()):
        if row == '\n':
            continue
        _, nums = row.split(':')
        have, winning = nums.split('|')
        cards[idx] = dict()
        cards[idx]['have'] = list()
        cards[idx]['winning'] = list()
        cards[idx]['winCount'] = 0
        cards[idx]['have'] = set([int(x) for x in have.split()])
        cards[idx]['winning'] = set([int(x) for x in winning.split()])
    return cards

cards = getCards()

for k in cards.keys():
    card = cards[k]
    matching = card['winning'] & card['have']
    cards[k]['winCount'] = len(matching)

    #  need recurse when brain better
    for _ in range(card['winCount']):
        for i in range(k + 1, k + len(matching) + 1):
            cards[i]['winCount'] += 1


accum = 0 
for k in cards.keys():
    print(cards[k]['winCount'])
    accum += cards[k]['winCount']
print(accum)


