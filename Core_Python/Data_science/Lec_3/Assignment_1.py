#!/usr/bin/env python3


import numpy as np
from imageio import *
from scipy.spatial.distance import pdist, squareform, cdist
# Read an JPEG image into a numpy array
u = np.array(imread('giraffe.jpg'))
v = np.array(imread('giraffe_tinted.jpg'))
def calculateDistance(image1, image2):
    distance = 0
    for i in range(len(image1)):
        for j in range(len(image2)):
            distance += (image1[i][j]-image2[i][j])**2
        distance = np.sqrt(distance)
        print(distance)
calculateDistance(u,v)

eclid = np.sqrt((u[:,0] - v[:,0])**2 + (u[:,1] - v[:,1])**2 + (u[:,2] - v[:,2])**2)
print(eclid)








'''def calculateDistance(i1, i2):
    return np.sum(np.sqrt((i1-i2)**2))'''


#dm = cdist(u, v, lambda u[i], v[j]: np.sqrt(((u-v)**2).sum()))

#print(dm)