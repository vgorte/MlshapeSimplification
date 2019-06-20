# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:18:30 2019

@author: Raoul
"""


def preprocessShapes(infile,outfile):

    stext1 = 'Brid'
    stext2 = 'No-Bird'
    stext3 = 'Iris-virginica'
    rtext1 = '0'
    rtext2 = '1'
    rtext3 = '2'

    fid = open(infile,"r")
    oid = open(outfile,"w")

    for s in fid:
        if s.find(stext1)>-1:
            oid.write(s.replace(stext1, rtext1))
        elif s.find(stext2)>-1:
            oid.write(s.replace(stext2, rtext2))
        elif s.find(stext3)>-1:
            oid.write(s.replace(stext3, rtext3))
    fid.close()
    oid.close()

import numpy as np
# Preprocessor to remove the test (only needed once)
#preprocessIris('/Users/srmarsla/Book/Datasets/Iris/iris.data','iris_proc.data')

shapes = np.loadtxt('iris_proc.data',delimiter=',')
shapes[:,:4] = shapes[:,:4]-shapes[:,:4].mean(axis=0)
imax = np.concatenate((shapes.max(axis=0)*np.ones((1,5)),np.abs(shapes.min(axis=0)*np.ones((1,5)))),axis=0).max(axis=0)
shapes[:,:4] = shapes[:,:4]/imax[:4]
print (shapes[0:5,:])

# Split into training, validation, and test sets
target = np.zeros((np.shape(shapes)[0],3));
indices = np.where(shapes[:,4]==0) 
target[indices,0] = 1
indices = np.where(shapes[:,4]==1)
target[indices,1] = 1
indices = np.where(shapes[:,4]==2)
target[indices,2] = 1

# Randomly order the data
order = list(range(np.shape(shapes)[0]))
np.random.shuffle(order)
shapes = shapes[order,:]
target = target[order,:]

train = shapes[::2,0:4]
traint = target[::2]
valid = shapes[1::4,0:4]
validt = target[1::4]
test = shapes[3::4,0:4]
testt = target[3::4]

#print train.max(axis=0), train.min(axis=0)

# Train the network
import mlp
net = mlp.mlp(train,traint,5,outtype='logistic')
net.earlystopping(train,traint,valid,validt,0.1)
net.confmat(test,testt)