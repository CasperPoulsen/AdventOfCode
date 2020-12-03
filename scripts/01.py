#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:19:10 2020

@author: casper
"""

L = [int(i) for i in open("../inputs/01", "r").read().split("\n")]

done = False
for i in L:
    for j in L:
        if i != j and i+j == 2020:
            print(f"{i} * {j} = {i*j}")
            done = True
            break
    if done:
        break

done = False
for x in L:
    for y in L:
        for z in L:
            if x != y and y != z and x+y+z == 2020:
                print(f"{x} * {y} * {z} = {x*y*z}")
                done = True
                break
        if done:
            break
    if done:
        break