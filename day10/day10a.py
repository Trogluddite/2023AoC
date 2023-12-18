#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"

inLines = list()

with open(filename) as file:
    data = file.readlines()
    for l in data:
        if len(l.strip()) == 0:
            continue
        inLines.append(l)

# - will becomee _ on left side
# | will becoome / on bottom side
dirs = {
        '-' : (1,0),    # right
        '_' : (-1,0),   # left
        '|' : (0, 1),   # up
        '/' : (0,-1),   # down
        'L' : (1,1),    # down-right
        'J' : (-1,1),   # down-left
        '7' : (-1,-1),  # up-left
        'F' : (-1,1),   # up-right
    }

def findStart(lines):
    for y, l in enumerate(lines):
        x = l.index('S') if 'S' in l else None
        if x:
            return (x,y)

class MazeNode:
    def __init__(self, typeChar, nodeX=None, nodeY=None):
        self.nodeX = nodeX
        self.nodeY = nodeY
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.typeChar  = typeChar
    def getAdjacents(self):
        pass
    def getMoves(self):
        pass

startPos = findStart(inLines)
mazeRoot = MazeNode(startPos[0], startPos[1], "S")



