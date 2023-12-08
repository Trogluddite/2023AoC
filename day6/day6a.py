#!/usr/bin/env python3
from math import floor
from functools import reduce

races = list(tuple())

with open('input.txt') as file:
    data = file.readlines()
    times =  [int(x) for x in data[0].split(":")[1].split(' ') if len(x) > 0 and x[0].isdigit()]
    distances =  [int(x) for x in data[1].split(":")[1].split(' ') if len(x) > 0 and x[0].isdigit()]

    races = zip(times, distances)

def countWins(raceTup):
    midpoint = floor(raceTup[0] / 2)
    wins = 0

    if raceTup[0] % 2 == 0:
        r = range(0, midpoint)
    else:
        r = range(0, midpoint + 1)
    for x in r:
        distance = x * (raceTup[0] - x)
        if distance > raceTup[1]:
            wins += 1
    wins *= 2
    if raceTup[0] % 2 == 0:
        wins += 1
    return wins

# part 1: produces correct ans: 303600
wins = list()
for tup in races:
    wins.append(countWins(tup))
print( reduce( lambda x, y: x * y, wins) )

### there must be a clever counting solution
# For 7, 9
# 7, 0, 7 * 0
# 6, 1, 6 * 1
# 5, 2, 5 * 2
# 4, 3, 4 * 3
# 3, 4, 3 * 4
# 2, 5, 2 * 5
# 1, 6, 1 * 6
# 0, 7, 0 * 7
#
# 1. count instances to max -- how to get count of losses?
# 2. euler to sum of digits from start, max
