#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:21:01 2019

@author: Raul, Saad 
"""

import math
import numpy as np

def computeLength(P1, P2):  
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]
    a = math.pow( (x1 - x2) , 2 )
    b = math.pow( (y1 - y2) , 2 )
    length = math.sqrt( a + b )
    return length

def computeAngle(first, second, third):
    P12 = computeLength(first, second)
    P13 = computeLength(first, third)
    P23 = computeLength(second, third)
    a = math.pow(P12,2)
    b = math.pow(P13,2)
    c = math.pow(P23,2)
    d = (a + b - c) / (2 * P12 * P13)
    angle = np.arccos(d)
    return angle
    
def findAngles(shape):
    result = []
    i = 0
    actualLength = len(shape) - 1 #ignoring the last entry as its repetitive first point
    while i < actualLength:
        first = shape[i]
        second = shape[(i + 1) % actualLength]
        third = shape[(i + 2) % actualLength]
        angle = computeAngle(first,second,third)
        result.append(angle)
        i += 1
    return result