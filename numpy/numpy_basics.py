# importing
import numpy as np
from tables import DataTypeWarning

### numpy basics
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