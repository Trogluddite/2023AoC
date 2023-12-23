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
    lineLen = len(inLines[0])
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
    def __init__(self, typeChar, nodeX=None, nodeY=None, parent=None):
        self.X = int(nodeX) if nodeX else None
        self.Y = int(nodeY) if nodeY else None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.typeChar  = typeChar
        self.parent = parent

def buildLeaves(node, grid):
    if node.typeChar == '.':
        return node
    # we've made a full cylce
    if node.parent and node.typeChar == 'S':
        return node

    x = node.X
    y = node.Y
    mL = grid[ y ][x-1]
    mR = grid[ y ][x+1]
    mU = grid[y-1][ x ]
    mD = grid[y+1][ x ]

    if mL == '-':
        mL = '_'
    if mD == '|':
        mD = '/'

    if mL != 'S':
        if mL == '.':
            node.left = None
        else:
            mx, my = dirs[mL]
            lX = x + mx
            lY = y + my
            node.left = MazeNode(grid[lX][lY], lX, lY, node)
    if mR != 'S':
        if mR == '.':
            node.right = None
        else:
            mx, my = dirs[mR]
            rX = x + mx
            rY = y + my
            node.right = MazeNode(grid[rX][rY], rX, rY, node)
    if mU != 'S':
        if mU == '.':
            node.up = None
        else:
            mx, my = dirs[mU]
            uX = x + mx
            uY = y + my
            node.up = MazeNode(grid[uX][uY], uX, uY, node)
    if mD != 'S':
        if mD == '.':
            node.down = None
        else:
            mx, my = dirs[mD]
            dX = x + mx
            dY = y + my
            node.down = MazeNode(grid[dX][dY], dX, dY, node)

    if node.left:
        node.left = buildLeaves(node.left, grid)
    if node.right:
        node.right = buildLeaves(node.right, grid)
    if node.up:
        node.up = buildLeaves(node.up, grid)
    if node.down:
        node.down = buildLeaves(node.down, grid)
    return node

startPos = findStart(inLines)
mazeRoot = MazeNode('S', startPos[0], startPos[1], None)
mazeRoot = buildLeaves(mazeRoot, inLines)
