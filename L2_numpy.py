import numpy as np
array1 = np.arange(1,11)
array2 = np.arange(81,101)
print(array1)
print(array2)
print(type(array1))

array3 = np.arange(1,25,4)
print(array3)


array4 = np.arange(0,101,5)#it will return the numbers bwtween 0 and 100 but onlyin intervals of 5
print(array4)

array5 = np.arange(0,101,5,dtype=float)#this will change the float
print(array5)


array6 = np.arange(0,25,6)
print(array6)

array7 = np.linspace(1,30,5)
print(array7)

array8 = np.linspace(1,90,4)
print(array8)