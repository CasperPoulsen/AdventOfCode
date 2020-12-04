#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:46:01 2020

@author: casper
"""

import re
import collections

def readInput(file):
    f = open("../inputs/"+file, "r")
    data = f.read().split("\n\n")
    f.close()
    data = [line.split() for line in data]
    data = [[i.split(":") for i in line] for line in data]
    dicts = [{i[0]:i[1] for i in line} for line in data]
    return dicts

def getValids(dicts, keys):
    count = 0
    for d in dicts:
        count += all(key in d for key in keys)
    return count

def getStrictValids(dicts):
    keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    count = 0
    for d in dicts:
        if all(key in d for key in keys):
            passes = 0
            for field, value in d.items():
                if field == 'byr':
                    try:
                        passes += (int(value) >= 1920 and int(value) <= 2002)
                    except:
                        pass
                elif field == 'iyr':
                    try:
                        passes += (int(value) >= 2010 and int(value) <= 2020)
                    except:
                        pass
                elif field == 'eyr':
                    try:
                        passes += (int(value) >= 2020 and int(value) <= 2030)
                    except:
                        pass
                elif field == 'hgt':
                    try:
                        val = int(value[:-2])
                        if value[-2:] == "cm":
                            passes += (val >= 150 and val <= 193)
                        elif value[-2:] == "in":
                            passes += (val >= 59 and val <= 76)
                    except:
                        pass
                elif field == 'hcl':
                    try:
                        match = re.match("^#[0-9a-f]{6}$", value)
                        passes += match is not None
                    except:
                        pass
                elif field == 'ecl':
                    try:
                        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        passes += value in colors
                    except:
                        pass
                elif field == 'pid':
                    try:
                        match = re.match("^[0-9]{9}$", value)
                        passes += match is not None
                    except:
                        pass
            count += passes == len(keys)
    return count

dicts = readInput("04")
keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

print(f"Part A: {getValids(dicts, keys)}")
print(f"Part B: {getStrictValids(dicts)}")