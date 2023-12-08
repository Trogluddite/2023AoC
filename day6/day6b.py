#!/usr/bin/env python3
from math import floor
from functools import reduce

race = tuple()

with open('input.txt') as file:
    data = file.readlines()
    time =  int( data[0].split(":")[1].replace(' ',''))
    distance = int( data[1].split(":")[1].replace(' ',''))
    race = (time, distance)

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

print(countWins(race))

# produces correct answer for my input: 23654842
# ... still feel like there's a more clever way to do this
