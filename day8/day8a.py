#!/usr/bin/env python3

import sys
from itertools import cycle

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

def walkAndCount():
    stepCount = 0
    currKey = 'AAA'
    dirIter = cycle(directions)
    while currKey != 'ZZZ':
        currKey = mappings[currKey][next(dirIter)]
        stepCount += 1
    return stepCount
print(walkAndCount())

# produces correct answer for part 1: 19241

