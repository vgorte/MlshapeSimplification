# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:18:30 2019

@author: Raoul
"""


def preprocessShapes(infile,outfile):

    stext1 = 'No-Brid'
    stext2 = 'Bird'
    rtext1 = '0'
    rtext2 = '1'

    fid = open(infile,"r")
    oid = open(outfile,"w")

    for s in fid:
        if s.find(stext1)>-1:
            oid.write(s.replace(stext1, rtext1))
        elif s.find(stext2)>-1:
            oid.write(s.replace(stext2, rtext2))
    fid.close()
    oid.close()

import numpy as np



angles = np.loadtxt('angles.data',delimiter=',')

print(angles)
angles[:,:12] = angles[:,:12]-angles[:,:12].mean(axis=0)
print(angles)
imax = np.concatenate((angles.max(axis=0)*np.ones((1,13)),np.abs(angles.min(axis=0)*np.ones((1,13)))),axis=0).max(axis=0)
angles[:,:12] = angles[:,:12]/imax[:12]
print (angles[0:13,:])

# Split into training, validation, and test sets
target = np.zeros((np.shape(angles)[0],3));
indices = np.where(angles[:,12]==0) 
target[indices,0] = 1
indices = np.where(angles[:,12]==1)
target[indices,1] = 1


# Randomly order the data
order = list(range(np.shape(angles)[0]))
np.random.shuffle(order)
angles = angles[order,:]
target = target[order,:]

train = angles[::2,0:12]
traint = target[::2]
valid = angles[1::12,0:12]
validt = target[1::12]
test = angles[3::12,0:12]
testt = target[3::12]

#print train.max(axis=0), train.min(axis=0)


# Train the network
import mlp
net = mlp.mlp(train,traint,5,outtype='logistic')
net.earlystopping(train,traint,valid,validt,0.1)
net.confmat(test,testt)