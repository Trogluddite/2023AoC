#!/usr/bin/env python3
from collections import defaultdict

adjacent = {(0, 1),(0, -1),(-1, 0),(1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)}

# build a 2d array of functions, each returns the character in the x,y position
def buildSchematic():
    schematic = defaultdict(lambda: defaultdict(lambda: '.'))
    for y, row in enumerate(open('input.txt').readlines()):
        for x, c in enumerate(row):
            schematic[y][x] = c
    return schematic

# generator to yield chars in schematic that are adjacent to x,y
def adjacentCells(x, y):
    for dx, dy in adjacent:
        c = schematic[y+dy][x+dx]
        if c != '.\r\n':
            yield c, (x+dx, y+dy)

# build dict with keys being the (x,y) set describing the location of a char
# and values being a dict with keys the starting position of a part num 
# and values the part num itself
def getParts():
    sHeight = len(schematic)
    sWidth = len(schematic[0])
    parts = defaultdict(lambda: defaultdict(set))

    for idxL in range( sHeight ):
        num = ''
        for idxC in range( sWidth ):
            c = schematic[idxL][idxC]
            if c.isdigit():
                num += c
            else:
                for i, c in enumerate(num):
                    for part, pos in adjacentCells( idxC + i - len(num), idxL):
                        if part in '.\r\n0123456789':
                            continue
                        # storing (idxC,idxL) to handle cases where 2 identical numbers are neidxCt to a part.
                        parts[part][pos].add(((idxC,idxL),int(num)))
                num = ''
    return parts

schematic = buildSchematic()
parts = getParts()

gearRatioAccum = 0
for nums in parts['*'].values():
    if len(nums) == 2:
        (_, a), (_, b) = nums
        gearRatioAccum += a * b
print(gearRatioAccum)
