# numpy.ndarray的矩陣運算

## 亂數產生二維矩陣

在 Python 中可用 numpy.random.randint() 亂數產生一個n維矩陣(ndarray).
以下是一個例子:


```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維矩陣
a=np.random.randint(1, 10, (3, 5));
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[2 9 5 7 9]
 [7 6 2 3 3]
 [2 8 1 9 7]]
(3, 5)
<class 'numpy.ndarray'>
```

## 轉置矩陣

numpy.ndarray 可以使用 tanspose() 函式得到一個轉置矩陣.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維矩陣
a=np.random.randint(1, 10, (3, 5));
print(a)
print(a.shape)
print(type(a))

#  transpose
b=a.transpose()
print(b)
print(b.shape)
```

以下是執行結果:
```
[[5 3 9 9 6]
 [6 2 9 4 4]
 [4 4 7 7 3]]
(3, 5)
<class 'numpy.ndarray'>
[[5 6 4]
 [3 2 4]
 [9 9 7]
 [9 4 7]
 [6 4 3]]
(5, 3)
```


## 反矩陣

使用 numpy.linalg.inv() 函式得到一個反矩陣.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維陣列
a=np.random.randint(1, 10, (5, 5))
print(a)

b=np.linalg.inv(a)
print(b)
```

以下是執行結果:
```
[[8 8 9 1 7]
 [5 7 9 5 6]
 [5 4 9 7 1]
 [1 7 6 3 3]
 [8 8 1 9 6]]
[[ 0.15303773 -0.1987789   0.09678711 -0.08427585  0.04624162]
 [ 0.08657792 -0.28315484  0.01551396  0.26363727  0.04774297]
 [-0.00210189  0.08317486  0.05164648 -0.01911721 -0.07977179]
 [-0.14062656  0.1362226   0.02682414 -0.04093684  0.04383946]
 [-0.10819738  0.42438194 -0.19857872 -0.1745571  -0.01111   ]]
```


## 矩陣相加

使用運算符號 + , 可以讓兩個大小相同的矩陣相加.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維陣列
a=np.random.randint(1, 10, (5, 5))
print(a)

b=np.random.randint(1, 10, (5, 5))
print(b)

print('-----------------------------')
print(a+b)
```

以下是執行結果:
```
[[1 5 3 3 8]
 [1 3 6 8 4]
 [7 8 4 4 3]
 [8 4 6 5 8]
 [1 5 1 1 9]]
[[8 6 1 8 4]
 [7 4 2 2 3]
 [7 1 6 3 1]
 [4 6 9 6 2]
 [5 7 9 5 5]]
-----------------------------
[[ 9 11  4 11 12]
 [ 8  7  8 10  7]
 [14  9 10  7  4]
 [12 10 15 11 10]
 [ 6 12 10  6 14]]
```



## 矩陣相乘

使用 numpy.dot() 函式可以進行矩陣相乘, 以下是一個例子:

```javascript
import numpy as np
from numpy.linalg import inv
from numpy import dot

# 建立一個 numpy.ndarray, 2維陣列
a=np.array([[1,2],[3,4]])
print(a)

# 計算反矩陣
b=inv(a)
print(b)

# 計算矩陣相乘
print('-----------------------------')
print(dot(a,b))
```

以下是執行結果:
```
[[1 2]
 [3 4]]
[[-2.   1. ]
 [ 1.5 -0.5]]
-----------------------------
[[  1.00000000e+00   1.11022302e-16]
 [  0.00000000e+00   1.00000000e+00]]
```
