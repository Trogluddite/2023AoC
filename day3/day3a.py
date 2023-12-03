#!/usr/bin/env python3

working_list = [] 

with open("input.txt", "r") as fileIn:
    for line in fileIn.readlines():
        if line == '':
            continue

print(sum(working_list))
