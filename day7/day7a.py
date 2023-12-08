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
    counts = dict()
    for c in handInst[0]:
        if counts.get(c, None):
            counts[c] += 1
        else:
            counts[c] = 1

    havePair = False
    have3ofKind = False
    have2Pair = False
    for _, v in counts.items():
        if v == 5:
            handBuckets['fiveOfKind'].append(handInst)
            return
        if v == 4:
            handBuckets['fourOfKind'].append(handInst)
            return
        if v == 3:
            have3ofKind = True
            continue
        if v == 2:
            if havePair:
                have2Pair = True
            else:
                havePair = True
            continue
    if have3ofKind and havePair:
        handBuckets['fullHouse'].append(handInst)
        return
    if have3ofKind:
        handBuckets['threeOfKind'].append(handInst)
        return
    if have2Pair:
        handBuckets['twoPair'].append(handInst)
        return
    if havePair:
        handBuckets['onePair'].append(handInst)
        return
    handBuckets['highCard'].append(handInst)

for h in hands:
    bucketHand(h)

for k,v in handBuckets.items():
    print(f'handType: {k}, hands of type: {v}')
