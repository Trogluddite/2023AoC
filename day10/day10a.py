#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"

inLines = list()

# pad the map enough to avoid dealing with bounds checking
with open(filename) as file:
    data = file.readlines()
    for l in data:
        if len(l.strip()) == 0:
            continue
        l = l.strip()
        l = '..' + l + '..'
        inLines.append(l)
    lineLen = len(inLines[0]) + 4
    inLines.append('.' *  lineLen)
    inLines.append('.' *  lineLen)
    inLines.insert(0, '.' * lineLen)
    inLines.insert(0, '.' * lineLen)

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
        '.' : (0,0),    # no movement
    }

def findStart(lines):
    for x, l in enumerate(lines):
        y = l.index('S') if 'S' in l else None
        if y:
            return (x,y)

class MazeNode:
    def __init__(self, typeChar, nodeX=None, nodeY=None):
        self.X = int(nodeX) if nodeX else None
        self.Y = int(nodeY) if nodeY else None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.typeChar  = typeChar

def buildLeaves(node, grid):
    if node.typeChar == '.' or node.typeChar == 'S':
        return

    x = node.X
    y = node.Y
    mL = grid[x-1][ 0 ]
    mR = grid[x+1][ 0 ]
    mU = grid[ 0 ][y+1]
    mD = grid[ 0 ][y-1]

    if mL == '-':
        mL = '_'
    if mD == '|':
        mD = '/'

    lX, lY = dirs[mL]
    node.left = MazeNode(grid[lX][lY], lX, lY)
    rX, rY = dirs[mR]
    node.right = MazeNode(grid[rX][rY], rX, rY)
    uX, uY = dirs[mU]
    node.up = MazeNode(grid[uX][uY], uX, uY)
    dX, dY = dirs[mD]
    node.down = MazeNode(grid[dX][dY], dX, dY)

    # cycle detection?
    buildLeaves(node.left, grid)
    buildLeaves(node.right, grid)
    buildLeaves(node.up, grid)
    buildLeaves(node.down, grid)

startPos = findStart(inLines)
mazeRoot = MazeNode('S', startPos[0], startPos[1])

buildLeaves(mazeRoot, inLines)

