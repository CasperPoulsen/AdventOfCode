#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:17:17 2020

@author: casper
"""

import os
import pandas as pd

colnames = ['min', 'max', 'char', 'code']
df = pd.read_csv('../inputs/02', sep=",", names=colnames)

count = 0
for index, row in df.iterrows():
    n = row['code'].count(row['char'])
    if n >= row['min'] and n <= row['max']:
        count += 1
        # print(f"{index}: {row['code']}")
print(f"sum: {count}")

count = 0
for index, row in df.iterrows():
    char = row['char']
    code = row['code']
    a = row['min']-1
    b = row['max']-1
    match = 0
    if a < len(code):
        match += code[a] == char
    if b < len(code):
        match += code[b] == char
    if match == 1:
        count += 1
        # print(f"B: {index}: {code}")
print(f"sum: {count}")