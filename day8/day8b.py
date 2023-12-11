#!/usr/bin/env python3

import sys
from itertools import cycle
from math import lcm  #py 3.9+

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"

directions = ''
mappings = dict()
with open(filename) as file:
    dataIter = iter(file.readlines())
    directions = next(dataIter)
    directions = directions.strip()
    for l in dataIter:
        if len(l.strip()) == 0:
            continue
        k, m = l.split('=')
        k = k.strip()
        mLft, mRgt = m.split(',')
        mLft = mLft.strip('() \n')
        mRgt = mRgt.strip('() \n')
        mappings[k] = dict()
        mappings[k]['L'] = mLft
        mappings[k]['R'] = mRgt

def getStartNodes():
    starts = list()
    for k in mappings.keys():
        if k[-1] == "A" :
            starts.append(k)
    return starts

def getCycleLength(startStr):
    cycleCount = 0
    dirIter = cycle(directions)
    nextStep = startStr
    while  nextStep[-1] != 'Z':
        nextStep = mappings[nextStep][next(dirIter)]
        cycleCount += 1
    return cycleCount

starts = getStartNodes()
cycleCounts = list()
for s in starts:
    cycleCounts.append(getCycleLength(s))

print(lcm(*cycleCounts))

#produces correct count for my input: 9606140307013
