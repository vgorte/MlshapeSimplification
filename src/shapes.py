# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:18:30 2019

@author: Raoul, Anna
"""

import numpy as np

np.random.seed(38)
angles = np.loadtxt('../assets/angles/angles_v2.txt',delimiter=',')

print(angles)
angles[:,:12] = angles[:,:12]-angles[:,:12].mean(axis=0)
print(angles)
imax = np.concatenate((angles.max(axis=0)*np.ones((1,13)),np.abs(angles.min(axis=0)*np.ones((1,13)))),axis=0).max(axis=0)
angles[:,:12] = angles[:,:12]/imax[:12]
print(angles[0:13,:])

# Split into training, validation, and test sets
target = np.zeros((np.shape(angles)[0],2))
indices = np.where(angles[:,12]==0)
target[indices,0] = 1
indices = np.where(angles[:,12]==1)
target[indices,1] = 1


# Randomly order the data
order = list(range(np.shape(angles)[0]))
np.random.shuffle(order)
angles = angles[order,:]
target = target[order,:]

train = angles[::2,0:4]
traint = target[::2]
valid = angles[1::4,0:4]
validt = target[1::4]
test = angles[3::4,0:4]
testt = target[3::4]

#print train.max(axis=0), train.min(axis=0)

# Train the network
import mlp
net = mlp.mlp(train,traint,10, 5,outtype='softmax')
net.earlystopping(train,traint,valid,validt,0.1)
net.saveModel("../assets/blobs/model.pkl")
net.confmat(test,testt)


# Test on some other data
net2 = mlp.mlp.loadModel("../assets/blobs/model.pkl")
test_data = np.loadtxt('../assets/angles/angles_test.txt',delimiter=',')
order2 = list(range(np.shape(test_data)[0]))
np.random.shuffle(order2)
test_target = np.zeros((np.shape(test_data)[0],2))

test_data = test_data[order2,:]
test_target= target[order2,:]

test_data = test_data[::2,0:4]
test_target = test_target[::2]

net2.confmat(test_data, test_target)