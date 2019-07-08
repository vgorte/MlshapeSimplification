import sys
import math
import os, random
import numpy as np
import matplotlib.pyplot as plt
import csv

import AngleFinder as AF

def randomNumber(type):
    return {
        'standard-normal': np.random.standard_normal(),
        'triangular': np.random.triangular(-2.1, 2.3, 2.5)
    }.get(type, np.random.uniform(-2.1, 2.5))


def randomRadian():
    deg = np.random.uniform(0, 360, 1)
    radian = deg * (math.pi / 180)
    return radian


def findRotationCenter(x, y):
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    centerX = np.int(x_sorted[-1]) - np.int(x_sorted[0])
    centerY = np.int(y_sorted[-1]) - np.int(y_sorted[0])
    return centerX, centerY


def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
    xr, yr = [], []

    for i in range(len(x)):
        xr.append(math.cos(theta) * (x[i] - xo) - math.sin(theta) * (y[i] - yo) + xo)
        yr.append(math.sin(theta) * (x[i] - xo) + math.cos(theta) * (y[i] - yo) + yo)
    return xr, yr


def extractAlteredCoordinates(shape, distType):
    x, y = [], []
    for v in shape:
        x.append(np.int(v[0]) + randomNumber(distType))
        y.append(np.int(v[1]) + randomNumber(distType))

    # join last point with the first point
    x[len(x) - 1] = x[0]
    y[len(y) - 1] = y[0]
    return x, y


def randomShapeFilePath():
    return "../Shapes/" + random.choice(os.listdir("../Shapes"))
    
def corssFilePath():
    return "../crossShapes/Shape7.csv"

def getRealBirdShape(i):
    return "../Shapes/BirdData/csv/{}.csv".format(i)


def main(crossPath, shapeFilePath, distType):
    for i in range(34):
        print(i)
        xy2DArrayGenerater = saveXYCoor(crossPath, distType)
        xy2DArrayConvertingToAngles = convertToAngles(xy2DArrayGenerater)
        print(xy2DArrayConvertingToAngles)
    
    
    
        #plt.plot(xr, yr)
        #plt.axis('off')
        #plt.savefig('filename.png', bbox_inches='tight')
        #plt.show()
        
        createDataset(xy2DArrayConvertingToAngles,"0")
        
    for i in range(33):
        path = getRealBirdShape(i+1)
        shape = np.genfromtxt(path, delimiter=',')
            
        x, y = extractAlteredCoordinates(shape, distType)
        xo, yo = findRotationCenter(x, y)
        rad = randomRadian()
        xr, yr = rotate(x, y, xo, yo, rad)
        
        result=[]
        i=0
        #save xr and yr coordinates in a 2D array
        while i < len(xr):
            temp = [xr[i], yr[i]]
            result.append(temp)
            i+=1
            
        cross = convertToAngles(result)
        
        createDataset(cross,"1")
        
        
        
        


#function that generate x/y coordinates and save them in a 2D array
def saveXYCoor(shapeFilePath, distType):
    resultXY=[]
    #generate random shapes/corners --> for later improvement for loop (run 30 times)
    for xnum in range(1):
        shape = np.genfromtxt(shapeFilePath, delimiter=',')
    
        x, y = extractAlteredCoordinates(shape, distType)
        xo, yo = findRotationCenter(x, y)
        rad = randomRadian()
        xr, yr = rotate(x, y, xo, yo, rad)

        i=0
        #save xr and yr coordinates in a 2D array
        while i < len(xr):
            temp = [xr[i], yr[i]]
            resultXY.append(temp)
            i+=1

        return resultXY

def createDataset(inputAngles, categorie):
   
    if os.path.isfile('./angles_v2.txt'):

        readFile = open("angles_v2.txt", "r")
        temp = readFile.read()
        readFile.close()
        
        writeFile = open("angles_v2.txt", "w")
        writeFile.write("")
        
    
        
        writeFile.write(temp  +  '\n')
        
        for i in inputAngles:     
            writeFile.write(str(i) + ",")
        writeFile.write(categorie)
        
        writeFile.close()
            
        
    else:
        writeFile = open("angles_v2.txt", "w")
        writeFile.write("")
        
    
                
        for i in inputAngles:     
            writeFile.write(str(i) + ",")
        writeFile.write(categorie)
        writeFile.close()
           
        writeFile.close()
    


    

#function that call the AngleFinder script to calculate the angle of the random corners
def convertToAngles(XYinput):
    result =  AF.main(XYinput)
    return result


#run the main
if (__name__ == "__main__"):
    crossPath = corssFilePath()
    shapeFile = randomShapeFilePath()
    distType = None
    if (len(sys.argv) == 2):
        distType = str(sys.argv[1])
    main(crossPath, shapeFile, distType)
