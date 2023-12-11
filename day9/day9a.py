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

def extrapolate(lineVals):
    lines = [lineVals]
    foundZeros = False
    while not foundZeros:
        currLine = lines[-1]
        nextLine = list()
        for idx, val in enumerate(currLine):
            if idx < len(lineVals)-1:
                nextLine.append(abs(val - lineVals[idx+1]))
        lines.append(nextLine)
        if all(x==0 for x in nextLine):
            foundZeros = True
    return(lines)

intVals = [int(x) for x in inLines[0].split() ]
print(extrapolate( intVals ))
