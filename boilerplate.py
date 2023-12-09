#!/usr/bin/env python3

import sys

if len(sys.argv()) > 1:
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

