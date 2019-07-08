#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 17:29:00 2019

@author: Saad (refactor) 
"""

def preprocessShapes(inFile,outFile):
    """Searches for 'No-Bird' and 'Bird' strings inside the inFile and 
        replaces them with 0 and 1 respectively to write them to outFile

        Parameters:
        inFile (string): Input file path
        outFile (string): Output file path
    """

    sText1 = 'No-Bird'
    sText2 = 'Bird'
    rText1 = '0'
    rText2 = '1'

    fid = open(inFile,"r")
    oid = open(outFile,"w")

    for s in fid:
        if s.find(sText1)>-1:
            oid.write(s.replace(sText1, rText1))
        elif s.find(sText2)>-1:
            oid.write(s.replace(sText2, rText2))
    fid.close()
    oid.close()

def convertRadiansToDegrees(inputArray):
    """Converts from radians to degrees

    Parameters:
        inputArray (array): Array of angles in radians
    
    Returns:
        outputArray (array): Array of angles in degrees
    """

    import math
    result = []
    for a in inputArray:
        converted = a * (180/math.pi)
        result.append(converted)
    return result

def getFileNamesFromDirectory(dirPath):
    """Gets only file names within the specified directory path

    Parameters: 
        dirPath (string): Directory path
    Returns:
        List of file names in the directory
    """
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]
    return onlyfiles
