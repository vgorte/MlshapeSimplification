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
    #print(d)
    angle = np.arccos(d)
    return angle
    
def findAngles(shape):
    result = []
    i = 0
    actualLength = len(shape) - 1 #ignoring the last entry as its repeatative first point
    while i < actualLength:
        first = shape[i]
        second = shape[(i + 1) % actualLength]
        third = shape[(i + 2) % actualLength]
        angle = computeAngle(first,second,third)
        result.append(angle)
        i += 1
    return result

def convertRadiansToDegrees(inputArray):
    result = []
    for v in inputArray:
        converted = v * (180/math.pi)
        result.append(converted)
    return result

def main(shape):
    from numpy import genfromtxt
    #shape = genfromtxt('../Shapes/Shape1.csv', delimiter=',')
    shape = shape
    print("shape: " , shape)
    angles = findAngles(shape)
    
    print('Angles in radians: ')
    print(angles)
    print('Angles in degrees: ')
    print(convertRadiansToDegrees(angles))

if (__name__ == "__main__"):
    main()
