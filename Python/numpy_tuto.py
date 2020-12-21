# Followed this tutorial : https://www.youtube.com/watch?v=GB9ByFAIAH4&ab_channel=KeithGalli
import numpy as np

# Initializing
np.zeros((2,3)) # [[0., 0., 0.] [0., 0., 0.]]
np.ones((4,2,2), dtype='int32') # [[[1, 1][1, 1]] [[1, 1][1, 1]] [[1, 1][1, 1]] [[1, 1][1, 1]]]
np.full((2,2), 99) # [[99., 99.][99., 99.]]
# Random
np.random.rand(2,2) # [[0.0249486  0.93588073] [0.811319   0.37099611]]
np.random.randint(7, size=(2,2)) # [[2 5][3 1][4 2]]
np.identity(3) # [[1. 0. 0.][0. 1. 0.][0. 0. 1.]]
#Complex
d = np.ones((5,5))
d[1:-1, 1:-1] = np.zeros((3,3))
d[2,2] = 9 # [[1. 1. 1. 1. 1.][1. 0. 0. 0. 1.][1. 0. 9. 0. 1.][1. 0. 0. 0. 1.][1. 1. 1. 1. 1.]]


# Getting information
a = np.array([[1,2,3], [9.1, 8.0, 7.0]])
a.ndim # Get dimension : 2
a.shape # Get shape : (2, 3)
a.dtype # Get type : float64
a.itemsize # Get size of data type : 8
a.size # Get number of items : 6
a.nbytes # Get toal number of bytes : 48


# Accessing or Changing elements, rows, columns, etc
b = np.array([ [1,2,3,4,5,6,7], [8,9,10,11,12,13,14] ])
# Accessing
b # [[ 1  2  3  4  5  6  7][ 8  9 10 11 12 13 14]]
b[1,5] # 13
b[-1, -2] # 13
b[0] # [1 2 3 4 5 6 7]
b[0, 3:] # [4 5 6 7]
b[:, 0] # [1, 8]
b[0, 1:6:2] # [2, 4, 6]
# Assigning 
b[1,5] = 20 # [[ 1  2  3  4  5  6  7][ 8  9 10 11 12 20 14]]
b[:,2] = [1,2] # [[ 1  2  1  4  5  6  7][ 8  9 2 11 12 20 14]]


# 3D
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
c # [ [ [1 2][3 4] ]  [ [5 6][7 8] ] ]
c[0] # [[1 2][3 4]]
c[0,1,1] # 4
c[:,1,:] # [ [3 4][7 8] ]
c[:,0,:] # [ [1 2][5 6] ]
c[:,0,1] # [2 6]
c[:,1,:] = [[9,9],[8,8]] # [[[1 2][9 9]] [[5 6][8 8]]]


# Simple Math
e = np.array([1,2,3,4])
f = np.array([1,0,1,0])
e + 2 # [5, 6, 7, 8]
e - 2 # [-1,  0,  1,  2]
e * 2 # [2, 4, 6, 8]
e / 2 # [0.5, 1. , 1.5, 2. ]
e + f # [2, 2, 4, 4]
e ** 2 # [1,  4,  9, 16]
np.cos(e) # [ 0.54030231, -0.41614684, -0.9899925 , -0.65364362]


# Simple Linear Algebra https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
g = np.ones((2,3)) 
h = np.full((3,2), 2)
np.matmul(g,h) # [[6., 6.][6., 6.]]
np.linalg.det(np.matmul(g,h)) # 0
# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse


# Statistics 
i = np.array([[1,2,3],[4,5,6]])
np.min(i) # 1
np.max(i, axis=1) # [3, 6]
np.sum(i, axis=0) # [5, 7, 9]


# Reorganazing arrays
j = np.array([[1,2,3,4],[5,6,7,8]])
k = np.array([[1,2,3,4],[5,6,7,8]])
l = j.reshape(8,1) # [[1][2][3][4][5][6][7][8]]
np.vstack([j,k]) # [[1 2 3 4][5 6 7 8][1 2 3 4][5 6 7 8]]
np.hstack([k,j]) # [[1 2 3 4 1 2 3 4][5 6 7 8 5 6 7 8]]


# Masking and indexing
j[j > 5] # [6 7 8]
j > 5 # [[False False False False][False  True  True  True]]
b[0][[1, 3, 5]] # [2 4 6]

print(b[0][[1, 3, 5]])
