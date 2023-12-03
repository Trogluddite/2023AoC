#!/usr/bin/env python3

digits = ['1','2','3','4','5','6','7','8','9','0']
partNums = list()

schematic = []

def checkIfPartNum(lineNum, stringStart, stringEnd):
    isPart = False
    
    # check left
    if stringStart > 0:
        if schematic[lineNum][stringStart - 1] != '.':
            return True
    
    # check right
    if stringEnd < (len(schematic[lineNum]) - 1):
        if schematic[lineNum][stringEnd + 1] != '.':
            return True

    # check line above
    if lineNum > 0:
        if stringStart > 0:
            if schematic[lineNum -1][stringStart - 1] != '.':
                return True
        for c in range(stringStart, stringEnd + 1):
            if schematic[lineNum -1][c] != '.':
                return True
        if stringEnd < (len(schematic[lineNum - 1]) - 1):
            if schematic[lineNum -1][stringEnd + 1] != '.':
                return True
    
    # check line below
    if lineNum < len(schematic) - 1:
        if stringStart > 0:
            if schematic[lineNum +1][stringStart - 1] != '.':
                return True
        for c in range(stringStart, stringEnd + 1):
            if schematic[lineNum +1][c] != '.':
                return True
        if stringEnd < len(schematic[lineNum - 1]):
            if schematic[lineNum +1][stringEnd + 1] != '.':
                return True
    return isPart


with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        schematic.append(list(line.strip('\n')))

for idxL, l in enumerate( schematic ):
    candidateStart = idxC = ptr = 0
   
    while idxC < len(l):
        c = l[idxC]
        if c in digits:
            ptr = candidateStart = idxC
            while ptr < len(l) - 1 and l[ptr + 1] in digits:
                ptr += 1
            idxC = ptr
            if(checkIfPartNum(idxL, candidateStart, ptr)):
                partNums.append( int(''.join(l[candidateStart:ptr+1])) )
        idxC+=1

print(sum(partNums))
