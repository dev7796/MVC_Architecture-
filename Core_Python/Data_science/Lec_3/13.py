# Distance between points

# SciPy defines some useful functions for computing distances between sets of points.

# The function scipy.spatial.distance.pdist computes the distance between all pairs of points in a given set

import numpy as np
from scipy.spatial.distance import pdist, squareform, cdist

# Create the following array where each row is a point in 2D space:
# [[0 1]
#  [1 0]
#  [2 0]]

# dist=((x1-x2)^2)+((y1-y2)^2)+((z1-z2)^2)

x = np.array([[0, 1], [1, 0], [2, 0]])
y = np.array([[1, 0], [2, 0], [1, 0]])
u = np.array([[1,1,1],[2,2,2]])
v = np.array([[3,2,2],[1,1,1]])
print(x)

# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
d = squareform(pdist(x, 'euclidean'))
print(d)
e = cdist(x,y,'euclidean')
print(e)
Y = cdist(x, y, 'minkowski', p=2.)
print(Y)
z = cdist(u, v, 'cityblock')
print("This is z",z)
Y = cdist(u, v, 'cosine')
print("This  is cosine",Y)
Y = cdist(u, v, 'canberra')
print("this is canberra",Y)
dm = cdist(u, v, lambda u, v: np.sqrt(((u-v)**2).sum()))
print("this is dm",dm)
# A similar function (scipy.spatial.distance.cdist) computes the distance between all pairs across two sets of points.
