import numpy as np
from tempfile import TemporaryFile

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
print(c)  
print(d)
print(a.shape, c.shape, d.shape)

print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)
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



