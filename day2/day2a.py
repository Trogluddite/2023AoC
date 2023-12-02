#!/usr/bin/env python3

games = dict()
validGameNums = []
maxColorVals = {
    'red' : 12,
    'green' : 13,
    'blue' : 14,
}
def checkGame(gameVals):
    pulls = gameVals.split(";")
    pValid = True;
    for p in pulls:
        colors = p.split(',')
        for c in colors:
            count, color = c.split()
            if int(count) > int(maxColorVals[color]):
                pValid = False
    return pValid

    
with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        lineParts = line.split(':')
        games[ lineParts[0].replace('Game ', '') ] = lineParts[1]
    for game, vals in games.items():
        if checkGame(vals):
            validGameNums.append(int(game))
print(sum(validGameNums))


