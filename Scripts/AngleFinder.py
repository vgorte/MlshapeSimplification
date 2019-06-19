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
    angle = np.arccos( d )
    return angle
    
def findAngles(shape):
    result = []
    i = 0
    while i < len(shape) - 2:
        first = shape[i] 
        second = shape[i+1]
        third = shape[i+2]
        angle = computeAngle(first,second,third)
        result.append(angle)
        i += 1
    first = shape[i] 
    second = shape[i+1]
    third = shape[1]
    angle = computeAngle(first,second,third)
    result.append(angle)
    return result

def main():
    from numpy import genfromtxt
    shape = genfromtxt('../Shapes/Shape1.csv', delimiter=',')
    angles = findAngles(shape)
    return angles

if (__name__ == "__main__"):
    main()

