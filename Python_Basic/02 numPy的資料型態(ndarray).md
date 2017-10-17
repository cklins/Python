# NumPy 的資料型態(ndarray)

## ndarray (n-dimensional array, 多維陣列)

### np.array([a1, a2, ..., an])

在 Python 中宣告1個 ndarray 變數可直接使用 numpy.array() 函式, 傳入一個 list, 產生 numpy.ndarray 物件.
以下是一個例子:


```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.array([1,3,4,2,1])
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[1 3 4 2 1]
(5,)
<class 'numpy.ndarray'>
```

### np.ndarray([n])

使用 numpy.ndarray() 函式, 傳入一個 list, 產生 numpy.ndarray 物件, 其建立的空間不設定初值, 保留原記憶體內容. 以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.ndarray([4])
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[  4.99006302e-322   8.50624127e-317   0.00000000e+000   8.50677881e-317]
(4,)
<class 'numpy.ndarray'>
```

### np.array([[a1, a2, ..., an], [b1, b2, ..., bn]])

若傳入1個二維的 list, 可產生一個 numpy.ndarray 二維array.
以下是一個例子:
```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維陣列
a=np.array([[1,2,3], [4,5,6]])
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[1 2 3]
 [4 5 6]]
(2, 3)
<class 'numpy.ndarray'>
```

### np.ndarray([n1, n2])

使用 numpy.ndarray() 函式, 傳入1個具有2個元素的 list, 產生二維 numpy.ndarray 物件, 其建立的空間不設定初值, 保留原記憶體內容. 以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.ndarray([2, 4])
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[  6.52166653e-322   0.00000000e+000   0.00000000e+000   0.00000000e+000]
 [  0.00000000e+000   9.68368666e-322   0.00000000e+000   0.00000000e+000]]
(2, 4)
<class 'numpy.ndarray'>
```


### np.arange(n)

用numpy.arange() 函式, 傳入1個整數, 產生 numpy.ndarray 物件.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.arange(10)
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[0 1 2 3 4 5 6 7 8 9]
(10,)
<class 'numpy.ndarray'>
```


### np.zeros(n)

用numpy.zeros() 函式傳入1個整數, 產生 numpy.ndarray 物件, 其內容皆為 0.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.zeros(5)
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[ 0.  0.  0.  0.  0.]
(5,)
<class 'numpy.ndarray'>
```

### np.zeros((n1, n2))

numpy.zeros() 函式傳入1個 tuple, 產生二維 numpy.ndarray 物件, 其內容皆為 0.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維陣列
a=np.zeros((3, 6))
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]]
(3, 6)
<class 'numpy.ndarray'>
```


### np.ones((n1, n2), dtype=...)

numpy.ones() 函式傳入1個 tuple 及 dtype, 產生二維 numpy.ndarray 物件, 其內容皆為整數 1.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 2維陣列
a=np.ones((5, 6), dtype='i')  #i表示整數, f表示浮點數
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]]
(5, 6)
<class 'numpy.ndarray'>
```


### np.identity(n)

用numpy.identity() 函式傳入1個整數, 產生二維 numpy.ndarray 物件, 其為 identity matrix.
以下是一個例子:

```javascript
import numpy as np

# 建立一個 numpy.ndarray, 1維陣列
a=np.identity(5)
print(a)
print(a.shape)
print(type(a))
```

以下是執行結果:
```
[[ 1.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.]
 [ 0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  1.]]
(5, 5)
<class 'numpy.ndarray'>
```


### np.random.rand(n)

用numpy.random.rand() 函式傳入1個整數, 產生具有n個元素的 numpy.ndarray 物件, 其內容0~1之間的亂數值.
以下是一個例子:

```javascript
import numpy as np

a=np.random.rand(100)
print(a)
print(type(a))
```

以下是執行結果:
```
[ 0.2991346   0.74401697  0.63462704  0.11551614  0.33416989  0.80046416
  0.8192799   0.98551388  0.56660632  0.76941815  0.55597497  0.75789947
  0.95360267  0.90524457  0.09178753  0.26963591  0.94576517  0.90993814
  0.69623877  0.4267368   0.33204156  0.22735945  0.42697972  0.99761283
  0.27962762  0.60726932  0.5418787   0.28089529  0.82913038  0.10848548
  0.34600251  0.92603974  0.70454015  0.06855234  0.07937503  0.02751803
  0.25667818  0.9276827   0.10389295  0.03430796  0.56813043  0.86195298
  0.22064887  0.07268116  0.77711934  0.30401609  0.03499319  0.71375205
  0.81555104  0.56787524  0.02186616  0.97919585  0.871268    0.3600212
  0.68575295  0.91326717  0.23282418  0.24134196  0.24818086  0.08298552
  0.53293094  0.9916617   0.89656833  0.66193404  0.08916261  0.80745972
  0.08501792  0.8967455   0.30934323  0.90868936  0.49271178  0.24259893
  0.72373833  0.1773391   0.44933169  0.5315861   0.024171    0.99680535
  0.19858978  0.39051926  0.03492929  0.63842901  0.89951966  0.48454254
  0.77079668  0.6518617   0.2813459   0.20687806  0.52215785  0.32020291
  0.32947037  0.34152522  0.42805247  0.22121175  0.78113234  0.55772508
  0.81358492  0.64160101  0.42855777  0.99492788]
<class 'numpy.ndarray'>
```


### np.random.randint(lowValue, highValue, n)

用numpy.random.randint() 函式傳入3個整數, 產生具有n個元素的 numpy.ndarray 物件, 其內容為lowValue ~ highValue之間的亂數整數值.
以下是一個例子:

```javascript
import numpy as np

a=np.random.randint(1, 50, 20)
print(a)
print(type(a))
```

以下是執行結果:
```
[ 5 45  3 34 35 20 20  2  6 34  1  2 16 13 10 35 41 49 32 22]
<class 'numpy.ndarray'>
```


### np.random.normal(mu, sigma, n)

用numpy.random.normal() 函式傳入3個整數, 產生具有n個元素的 numpy.ndarray 物件, 其內容為平均數為mu, 標準差為sigma, 共n個值的常態分配的亂數.
以下是一個例子:

```javascript
import numpy as np

a=np.random.normal(60, 15, 100)  #平均60, 標準差15, 共100個亂數
a=a.astype(int)   #轉成整數
a=a.clip(0, 100)  #限定範圍邊界
print(a)
print(type(a))
```

以下是執行結果:
```
[48 50 36 57 66 24 69 54 76 47 52 75 53 61 64 53 72 31 65 62 62 58 52 42 51
 58 67 62 69 67 72 76 41 44 57 44 62 69 32 46 45 43 48 54 74 57 63 59 37 44
 48 84 75 55 53 47 43 36 52 83 68 72 34 65 61 93 59 64 64 98 71 58 38 46 69
 64 48 49 65 54 34 54 84 40 58 72 62 49 58 49 73 61 99 45 67 46 61 70 32 40]
<class 'numpy.ndarray'>
```


### reshape()

用 ndarray 的 reshape() 函式可改變矩陣維度, 以下是一個例子:

```javascript
import numpy as np

# 建立一個 1維陣列 (陣列尺寸1*50)
a=np.random.randint(1, 100, (1, 50))
#或是寫成 a=np.random.randint(1, 100, 50)

print(a)
print(a.shape)
print(type(a))

# 將a轉為2維陣列
b=a.reshape(5, 10)
print(b)
print(b.shape)
```

以下是執行結果:
```
[[83 75  6 98 18 88 99 19  8 99 29 56 98 12 85 13 88 41 82 22 87 65 71 61
  58 43  7  6 21 49 75 27  4 65 56 63 60 47 99 91 61 47 64 63 62 77 28 65
  41 64]]
(1, 50)
<class 'numpy.ndarray'>
[[83 75  6 98 18 88 99 19  8 99]
 [29 56 98 12 85 13 88 41 82 22]
 [87 65 71 61 58 43  7  6 21 49]
 [75 27  4 65 56 63 60 47 99 91]
 [61 47 64 63 62 77 28 65 41 64]]
(5, 10)
```
