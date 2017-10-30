import numpy as np
from tempfile import TemporaryFile
import matplotlib.pyplot as plt

print (np.zeros((3, 4)))
print (np.ones((3, 4)))
print (np.full((3, 4), 17))
print (np.eye(3))


print (np.linspace(1, 10, num=10))

#矩陣運算
a = np.array([[1,5],
           [2,6],[4,3]])
b = np.arange(4).reshape((2,2))

#print(np.dot(a,b))
#print(a.dot(b))

#矩陣求和,最小,最大(by rwa or column)
a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.sum(a,axis=1))
print(np.sum(a,axis=0))
print(np.min(a,axis=0))
print(np.max(a,axis=0))
#axis=0 上->下  axis=1 左->右

a= np.arange(14,2,-1).reshape((3,4))
print(a)
print(np.argmin(a))
print(np.argmax(a))
print(np.mean(a))
print(a.mean())
print(np.median(a))
print(np.cumsum(a))
print(np.diff(a))
print(np.sort(a))
print(np.sort(a,axis=None))

#矩陣transpose
print(np.transpose(a))
print(a.T)

a = np.arange(10).reshape((1,10))
b = np.transpose(a)
b.shape

# 建立一個 numpy.ndarray, 2維矩陣
a=np.random.randint(1, 10, (3, 3));
print(a)

#  transpose
#b=a.transpose()
b=np.linalg.inv(a)
print(b)
print (a.dot(b))

#array index
a=np.arange(3,15).reshape((3,4))
print(a)
print(a[1][1])
print(a[1,1])
print(a[:,1])
print(a[1,0:3])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"

for row in a:
    print(row)
    
for column in a.T:
    print(column)

print(a.flatten())
for item in a.flat:
    print(item)
    
#array merage
a=np.array([1,1,1])
b=np.array([2,2,2])
c=np.vstack((a,b)) #vertical stack
d=np.hstack((a,b)) #horizontal stack
print(a.shape, c.shape, d.shape)

print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)

#單一維度作完transpose仍為一樣
print(a.T)
print(a[:,np.newaxis])
print(a[:,np.newaxis].shape)

a=np.array([1,1,1])[:,np.newaxis]
b=np.array([2,2,2])[:,np.newaxis]
d=np.hstack((a,b)) #horizontal stack
print(d)

#axis=0 上->下  axis=1 左->右
c = np.concatenate((a,b,b,a),axis=1)
print(c)

#array分割
a=np.arange(12).reshape((3,4))
print(np.split(a,2,axis=1))

#compile error
print(np.split(a,2,axis=1))

#array不等項分割
print(np.array_split(a,3,axis=1))

print(np.vsplit(a,3))
print(np.hsplit(a,2))

#array copy
a=np.arange(4)
b=a
c=a
d=b
a[0]=11
b is a

b = a.copy() #deep copy
b is a

#HW0
a=np.random.randint(1,10,(1,50))
b=np.random.randint(1,5,(50,10))
c=a.dot(b)
d=np.sort(c,axis=None)

np.savetxt('./result.txt',d,delimiter=',',fmt='%-3.0f')


x, y = np.meshgrid(np.arange(-3, 4), np.arange(-2,3))
contor = np.sqrt(x ** 2 + y ** 2)
plt.imshow(contor)
plt.colorbar()

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)


xvalues = np.array([1,2,3,4]);
yvalues = np.array([5,6,7]);
xx, yy = np.meshgrid(xvalues, yvalues)
print(xx)
print(yy)
plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

s = "hello"
print(s.capitalize())  # Capitalize a string; prints "Hello"
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))     # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"


animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"


d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"


d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"




a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"


import os

print(dir(os))

print(os.getcwd())