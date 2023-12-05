#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Alamanc:
    seeds: List[int] = field(default_factory=list)
    seed_to_soil: List[Dict[str, int]] = field(default_factory=list)
    soil_to_fertilizer: List[Dict[str, int]] = field(default_factory=list)
    fertilizer_to_water: List[Dict[str, int]] = field(default_factory=list)
    water_to_light: List[Dict[str, int]] = field(default_factory=list)
    light_to_temp: List[Dict[str, int]] = field(default_factory=list)
    temp_to_humidity: List[Dict[str, int]] = field(default_factory=list)
    humidity_to_location: List[Dict[str, int]] = field(default_factory=list)

# build a 2d array of functions, each returns the character in the x,y position
def getAlmanac():
    alm = Alamanc()
    mapType = ''
    for idx, row in enumerate(open('input.txt').readlines()):
        if idx == 0:
            alm.seeds = [int(x.strip()) for x in row.split(':')[1].split(' ') if x != '']
            continue
        if row == '\n':
            continue
        if 'map' in row:
            mapType, _ = row.split(' ')
            continue
        if row == '\n':
            continue
        destStart, sourceStart, rangeLen = row.split(' ')
        match mapType:
            case 'seed-to-soil':
                alm.seed_to_soil.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'soil-to-fertilizer':
                alm.soil_to_fertilizer.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'fertilizer-to-water':
                alm.fertilizer_to_water.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'water-to-light':
                alm.water_to_light.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'light-to-temperature':
                alm.light_to_temp.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'temperature-to-humidity':
                alm.temp_to_humidity.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
            case 'humidity-to-location':
                alm.humidity_to_location.append( {'destStart': int(destStart), 'sourceStart' : int(sourceStart), 'rangeLen' :int(rangeLen)} )
    return alm

alm = getAlmanac()
print(alm)
