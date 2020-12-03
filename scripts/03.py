#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:24:39 2020

@author: casper
"""

import numpy as np

f = open("../inputs/03", "r")
L = f.read().splitlines()

data = np.asarray([[0 if char == '.' else 1 for char in line] for line in L])

def countTrees(data, right=3, down=1):
    height, width = data.shape
    count = 0
    x, y = (0, 0)
    while y < height -1:
        y += down
        x = (y * right) % width
        count += data[y, x]
    return count

print(f"Part 1: {countTrees(data)}")

patterns = [(1,1), (3,1), (5,1), (7,1), (1,2)]

results = [countTrees(data, right, down) for right, down in patterns]

print(f"Part 2: {np.prod(results)}")