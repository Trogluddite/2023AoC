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
cardRanks = dict(zip( list('23456789TJQKA'), range(1,14)))
for k,v in handBuckets.items():
    # sort buckets by first card in hand, ranked by cardRank
    # higher card gets higher rank #
    # FIXME: bug here; if first card matches, it should sort based on second card
    handBuckets[k] =  sorted(handBuckets[k], key=(lambda h: cardRanks[ h[0][0] ]))

# generator to rank all hands, where higher rank is later in list
# and thus corresponds to a higher enumerated value
keyOrder = ['fiveOfKind', 'fourOfKind', 'fullHouse', 'threeOfKind', 'twoPair', 'onePair', 'highCard']
keyOrder.reverse()
def rankedHands():
    for k in keyOrder:
        for x in iter( handBuckets[k] ):
            yield x

handVals = list()
for k, h in enumerate(rankedHands()):
    print(f'rank: {(k+1)}, hand: {h}')
for r, h in enumerate(rankedHands()):
    # r+1 is hand ranking
    # h[1] is hand bid
    handVals.append( (r+1) * (h[1]) )

print(handVals)
print(sum(handVals))
