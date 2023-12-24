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
        '-' : (0,1),    # right
        '_' : (0,-1),   # left
        '|' : (-1, 0),  # up
        '/' : (1, 0),   # down
        'L' : (0,1),    # down-right
        'J' : (0,-1),   # down-left
        '7' : (0,-1),  # up-left
        'F' : (0,1),   # up-right
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
    if node.parent:
        print(f'parent coords {node.parent.X, node.parent.Y}')
    else:
        print('must be the root!')

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
        print(f'move L char: {mL}')
        if mL == '.':
            node.left = None
        else:
            mx, my = dirs[mL]
            lX = x + mx
            lY = y + my
            node.left = MazeNode(grid[lX][lY], lX, lY, node)
    if mR != 'S':
        print(f'move R char: {mR}')
        if mR == '.':
            node.right = None
        else:
            mx, my = dirs[mR]
            rX = x + mx
            rY = y + my
            node.right = MazeNode(grid[rX][rY], rX, rY, node)
    if mU != 'S':
        print(f'move U char: {mU}')
        if mU == '.':
            node.up = None
        else:
            mx, my = dirs[mU]
            uX = x + mx
            uY = y + my
            node.up = MazeNode(grid[uX][uY], uX, uY, node)
    if mD != 'S':
        print(f'move D char: {mD}')
        if mD == '.':
            node.down = None
        else:
            mx, my = dirs[mD]
            dX = x + mx
            dY = y + my
            node.down = MazeNode(grid[dX][dY], dX, dY, node)

    if node.left:
        print(f"get left children, from {node.left.X, node.left.Y}")
        node.left = buildLeaves(node.left, grid)
    if node.right:
        print(f'build right children, from {node.right.X, node.right.Y}')
        node.right = buildLeaves(node.right, grid)
    if node.up:
        print(f'build up children, from {node.up.X, node.up.Y}')
        node.up = buildLeaves(node.up, grid)
    if node.down:
        print(f"build down children, from {node.down.X, node.down.Y}")
        node.down = buildLeaves(node.down, grid)
    return node

def printChildren(node, depth=0):
    prependSpaces = ' ' * depth

    nextDepth = depth + 1
    if node.left:
        print(f'LEFT  {depth}: {prependSpaces} {node.left.X, node.left.Y, node.left.typeChar}')
        printChildren(node.left, nextDepth)
    if node.right:
        print(f'RIGHT {depth}: {prependSpaces} {node.right.X, node.right.Y, node.right.typeChar}')
        printChildren(node.right, nextDepth)
    if node.up:
        print(f'UP    {depth}: {prependSpaces} {node.up.X, node.up.Y, node.up.typeChar}')
        printChildren(node.up, nextDepth)
    if node.down:
        print(f'DOWN  {depth}: {prependSpaces} {node.down.X, node.down.Y, node.down.typeChar}')
        printChildren(node.down, nextDepth)

startPos = findStart(inLines)
mazeRoot = MazeNode('S', startPos[0], startPos[1], None)
mazeRoot = buildLeaves(mazeRoot, inLines)
printChildren(mazeRoot)
for x in inLines:
    print(x)
