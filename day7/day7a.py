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

# build lists of each hand type;
# E.G., all 'five of a kind' hands go in the same bucket
for h in hands:
    bucketHand(h)

# sort each bucket; sort key is assigned to each hand such that:
# 1. each card gets assigned a value equal to place value, times cardValue
# 2. cards are summed
# 3. use this as the hand's sorting key (see Lambda)
# rank-power is chosen such that no number of sums from the lower rank can equal
# the value of a the smallest card in the higher rank ... ^100 is a guess
cardValue = dict(zip( list('23456789TJQKA'), range(1,14)))
handLen = 5
rankPower = 100
for k,v in handBuckets.items():
    handBuckets[k] = sorted(handBuckets[k],
                            key=lambda h:
                                sum([(i+1) * ((rankPower**(handLen-i)) * cardValue[v]) for i,v in enumerate(h[0])])
                            )


# generator to rank all hands, where higher rank is later in list
# and thus corresponds to a higher enumerated value
keyOrder = ['fiveOfKind', 'fourOfKind', 'fullHouse', 'threeOfKind', 'twoPair', 'onePair', 'highCard']
keyOrder.reverse()
def rankedHands():
    for k in keyOrder:
        for x in iter( handBuckets[k] ):
            yield x

for b in handBuckets.keys():
    print(f'handType: {b}, instances: {handBuckets[b]}')
# finally, get all of the hand values, and return their sums
handVals = list()
for r, h in enumerate(rankedHands()):
    # r+1 is hand ranking
    # h[1] is hand bid
    print(r+1, h, (r+1) * h[1])
    handVals.append( (r+1) * (h[1]) )

print(sum(handVals))

# produces correct part A answer:
# 253933213
