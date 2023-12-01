#!/usr/bin/env python3

nums = ['1','2','3','4','5','6','7','8','9','0']
filteredInts = list()

def filterFun(val):
    if val in nums:
        return True
    else: 
        return False

with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        if line == '':
            continue
        filteredChars = filter(filterFun, line)
        intStr = ''
        for char in filteredChars:
            intStr += char
        try:
            intStr = f'{intStr[0]}{intStr[-1]}'
            filteredInts.append(int(intStr))
        finally:
            continue

print(sum(filteredInts))
