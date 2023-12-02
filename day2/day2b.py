#!/usr/bin/env python3

games = dict()
gamePowers = []

def getMaxCounts(game):
    maxVals = {
        'red' : 0,
        'green' : 0,
        'blue' : 0,
    }
    pulls = game.split(';')
    for p in pulls:
        colors = p.split(',')
        for c in colors:
            count, color = c.split()
            if int(count) > int(maxVals[color]):
                maxVals[color] = int(count)
    return maxVals

    
with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        lineParts = line.split(':')
        games[ lineParts[0].replace('Game ', '') ] = lineParts[1]
    for game, vals in games.items():
        counts = getMaxCounts(vals)
        power = counts['red'] * counts['green'] * counts['blue']
        gamePowers.append(power)
print(sum(gamePowers))


