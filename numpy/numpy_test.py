import numpy as np
from tempfile import TemporaryFile
import matplotlib.pyplot as plt

print (np.zeros((3, 4)))
print (np.ones((3, 4)))
print (np.full((3, 4), 17))


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