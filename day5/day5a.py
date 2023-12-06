#!/usr/bin/env python3

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Alamanc:
    propertyMappings = {
            'seeds' : 'seed_to_soil',
            'soil' : 'soil_to_fertilizer',
            'fertilizer' : 'fertilizer_to_water',
            'water' : 'water_to_light',
            'light' : 'light_to_temp',
            'temp' : 'temp_to_humidity',
            'humidity' : 'humidity_to_location',
            }
    seeds: List[int] = field(default_factory=list)
    seed_to_soil: List[Dict[str, int]] = field(default_factory=list)
    soil_to_fertilizer: List[Dict[str, int]] = field(default_factory=list)
    fertilizer_to_water: List[Dict[str, int]] = field(default_factory=list)
    water_to_light: List[Dict[str, int]] = field(default_factory=list)
    light_to_temp: List[Dict[str, int]] = field(default_factory=list)
    temp_to_humidity: List[Dict[str, int]] = field(default_factory=list)
    humidity_to_location: List[Dict[str, int]] = field(default_factory=list)

    def getDestinationMaps(self, sourceProp, sourceVals):
        destProp = self.__getattribute__(self.propertyMappings[sourceProp])
        sourceMappings = defaultdict(int)
        for v in sourceVals:
            sourceMappings[v] = v

        inst = 0
        for mapInstance in destProp:
            rangeLen = mapInstance['rangeLen']
            #sourceRange = list(range(mapInstance['sourceStart'], mapInstance['sourceStart'] + rangeLen))
            #destRange = list(range(mapInstance['destStart'], mapInstance['destStart'] + rangeLen))

            for v in sourceVals:
                if v >= mapInstance['sourceStart'] and v <= mapInstance['sourceStart'] + rangeLen:
                    valIdx = v - mapInstance['sourceStart']
                else:
                    valIdx = None
                if valIdx is not None:
                    sourceMappings[v] = mapInstance['destStart'] + valIdx
            inst += 1
                    
        return sourceMappings

# build a 2d array of functions, each returns the character in the x,y position
def buildAlmanac():
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

alm = buildAlmanac()

def unpack(map):
    return [map[k] for k in map.keys()]

seed_to_soil_map = alm.getDestinationMaps('seeds', alm.seeds)
soil_to_fertilizer_map = alm.getDestinationMaps('soil', unpack(seed_to_soil_map))
fertilizer_to_water_map = alm.getDestinationMaps('fertilizer', unpack(soil_to_fertilizer_map))
water_to_light_map = alm.getDestinationMaps('water', unpack(fertilizer_to_water_map))
light_to_temp_map = alm.getDestinationMaps('light', unpack(water_to_light_map))
temp_to_humidity_map = alm.getDestinationMaps('temp', unpack(light_to_temp_map))
humidity_to_location_map = alm.getDestinationMaps('humidity', unpack(temp_to_humidity_map))

locations = print(min(  [v for _,v in enumerate(humidity_to_location_map)] ))
# 71710860 for my input it too low:w
