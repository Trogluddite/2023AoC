#!/usr/bin/env python3

### Part 2 notes
# for part two, we need to replace number-describing strings with a coresponding single-digit character
# there isn't a rule specified for cases wehre the num-describing strings overlap, but I see five possiblitiles
# 1. 'eightwo' -> 'eigh2'   (take last)
# 2. 'eightwo' -> 'eigh2'   (take smaller value)
# 3. 'eightwo' -> '8wo'     (take first)
# 4. 'eightwo' -> '8wo'     (take larger value)
# 5. 'eightwo' -> '82'      (take both)
# for the test input, options 3,4, and 5 all work, we I'll have to try them all
# first attempt (option 3, take first) doesn't work on full input

nums = ['1','2','3','4','5','6','7','8','9','0']
# used for replacements on options 1-4
numStrings = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
# for option 5: these replacement strings will preserve the first/last character so that
# we can store both nubmers when they overlap
nonStompNumStrings = {
    'one':'o1e',
    'two':'t2o',
    'three':'t3e',
    'four':'f4r',
    'five':'f5e',
    'six':'s6x',
    'seven':'s7n',
    'eight':'e8t',
    'nine':'n9e',
}

# 'take both' replacement
def rewriteNumStrings(inputStr):
    for key, val in nonStompNumStrings.items():
        inputStr = inputStr.replace(key,val)
    return inputStr

filteredInts = list()
with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        line = rewriteNumStrings(line)
        filteredChars = list(filter((lambda x : True if x in nums else False), line))
        try:
            filteredChars = f'{filteredChars[0]}{filteredChars[-1]}'
            filteredInts.append(int(filteredChars))
        except:
            continue
print(sum(filteredInts))

# 'take first' replacement
# NOTE: this worked on the test input, but not the full input
#def rewriteNumStrings(inputStr):
#    rewriteIdxs = dict()
#    for key in numStrings.keys():
#        foundIdx = inputStr.find(key)
#        if foundIdx >= 0:
#            rewriteIdxs[foundIdx] = key
#    sortedIdxs = list(rewriteIdxs.keys())
#    sortedIdxs.sort()
#    for idx in sortedIdxs:
#        strToReplace = rewriteIdxs[idx]
#        inputStr = inputStr.replace(rewriteIdxs[idx], numStrings[strToReplace])
#    return inputStr


