import numpy as np#np is the nickname
array1 = np.ones((6,2),dtype=int)#creates array of 1s (3 rows and 5 coloumns)
print(array1)
print(type(array1))
print(":array 1")

array2 = np.zeros((3,7),dtype=int)
print(array2)
print(type(array2))
print(":array 2")

print("array 1s dimensions:",array1.ndim)
print("array 1s rows and coloumns:",array1.shape)
print("array 2s dimensions:",array2.ndim)
print("array 2s rows and coloumns:",array2.shape)