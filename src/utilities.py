#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 17:29:00 2019

@author: Saad (refactor) 
"""

def preprocessShapes(inFile,outFile):
    """Searches for 'No-Bird' and 'Bird' strings inside the inFile and 
        replaces them with 0 and 1 to write them to outfile

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