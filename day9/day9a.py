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

def reduceVals(lineVals):
    lines = [lineVals]
    foundZeros = False
    while not foundZeros:
        newLine = list()
        currLine = lines[-1]
        pairs = [(x-1, x) for x in range(1,len(currLine))]
        for p in pairs:
            newLine.append( currLine[p[1]] - currLine[p[0]] )
        lines.append(newLine)
        if all(x==0 for x in newLine):
            foundZeros = True
    return(lines)

def prependStarts(lines):
    for lineNum in reversed(range(1, len(lines))):
        if lineNum == len(lines) - 1:
            lines[lineNum].insert(0, 0)
        lines[lineNum - 1].insert(0, lines[lineNum-1][0] - lines[lineNum][0])
    return lines

extrapolatedVals = list()
for il in inLines:
    intVals = [int(x) for x in il.split() ]
    reducedIl = reduceVals(intVals)
    prepended = prependStarts(reducedIl)
    extrapolatedVals.append( prepended[0][0] )

print(sum(extrapolatedVals))
