#!/usr/bin/env python3

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
        cards[idx]['have'] = [int(x) for x in have.split()]
        cards[idx]['winning'] = [int(x) for x in winning.split()]
    return cards

cards = getCards()
for k in cards.keys():
    for num in cards[k]['have']:
        if num in cards[k]['winning']:
            cards[k]['winCount'] += 1

accum = 0
for x in cards.keys():
    count = cards[x]['winCount']
    if count < 2:
        accum += count
    else:
        accum += 2 ** (cards[x]['winCount'] - 1)
print(accum)
