# importing
import numpy as np
from tables import DataTypeWarning

##### Numpy Basics #####
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*15 vector

print(array.shape)

a = array.reshape(3,5)
print("a shape:",a.shape)
print(a)
print("dimension",a.ndim)

print("data type",a.dtype.name)
print("size",a.size)

print("type:",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print("array1 shape:",array1.shape)

zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)

np.ones((3,4))

np.empty((3,4))

a = np.arange(10,50,5) # Increases by 5 from 10 to 50.
print(a)

a = np.linspace(10,50,20)
print(a)

### numpy basic operations
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a<2)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

# element wise product
print(a*b)

# matrix product
print(a.dot(b.T))

print(np.exp(a))

a = np.random.random((5,5)) # Generates a 5 by 5 array of random 0 and 1.

print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis=0)) # sum of colons
print(a.sum(axis=1)) # sum of lines

print(np.sqrt(a)) # square root
print(np.square(a)) # a**2

print(np.add(a,a))

##### Indexing and Slicing #####

array = np.array([1,2,3,4,5,6,7]) # vector dimension = 1
print(array[0])

print(array[0:4])

reverse_array = array[::-1]
print(array)
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # vector dimension = 2
print(array1[1,1])
print(array1[:,1])

print(array1[1,1:4])

print(array1[-1,:])
print(array1[:,-1])


#### Shape Manipulation #####
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten
a = array.ravel() # [1,2,3],[4,5,6],[7,8,9] > [1 2 3 4 5 6 7 8 9]
print(a)

array2 = a.reshape(3,3)
print(array2)

arrayT = array2.T # transpose
print(arrayT)
print(arrayT.shape)

# Difference between reshape() and resize() methods
array5 = np.array([[1,2],[3,4],[4,5]])
# reshape()
print(array5.reshape(2,3)) # array5 didn't changed
print(array5)
# resize()
array5.resize(2,3)
print(array5)


##### Stacking Arrays #####
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# vertical stacking
# array([1,2],
#       [3,4])
# array([-1,-2],
#       [-3,-4])

array3 = np.vstack((array1,array2))
print(array3)

# horizontal stacking
# array([[1,2],[-1,-2],
#       [3,4],[-3,-4]])

array4 = np.hstack((array1,array2))
print(array4)