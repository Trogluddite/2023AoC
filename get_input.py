#!/usr/bin/env python3
import requests
import sys
import os
 
sessionToken = os.getenv('AOC_TOKEN')

YEAR=2023

def get_input(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    headers = {'Cookie': f'session={sessionToken}'}
    r = requests.get(url, headers=headers)
 
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")

print(get_input(sys.argv[1]))
