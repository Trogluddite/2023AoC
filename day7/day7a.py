#!/usr/bin/env python3

hands = list(tuple())
handBuckets = {
        "fiveOfKind"    : list(),
        "fourOfKind"    : list(),
        "fullHouse"     : list(),
        "threeOfKind"   : list(),
        "twoPair"       : list(),
        "onePair"       : list(),
        "highCard"      : list(),
    }

with open('input.txt') as file:
    data = file.readlines()
    for l in data:
        if len(l.strip()) == 0:
            continue
        hand, bid = l.split(' ')
        hands.append((hand, int(bid)))

def bucketHand(handInst):
    hand = ''.join(handInst[0].sorted())
