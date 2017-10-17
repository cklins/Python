# 用 numpy.genfromtxt() 讀檔案

## 準備 CSV 格式檔案

以下是一個 csv 格式資料, 每列代表一個學生的成績資料, 一個成績資料項目間以逗號隔開.
其項目意義分別為「序號」,「姓名」,「性別」,「國文」,「英文」,「數學」,「社會」,「自然」及「寫作」.
<p>
資料檔名稱為「scores.csv」, 和 Python 測試程式放在同一個資料夾中.

```
1,王小明,男,46,56,42,48,37,10
2,陳小華,男,48,51,39,48,43,10
3,劉小杰,男,50,52,47,41,42,8
  .
  .
  .
402,周小花,女,35,35,48,27,28,8
```

## 讀取一個欄位資料

在 numpy.genfromtxt() 中, 使用 usecols 參數指定取出的欄位編號, 即可取出特定欄位. 以下是一個例子:

```javascript
import numpy
#只讀取第1個欄位內容 (欄位編號從0開始)
names=numpy.genfromtxt('scores.csv', dtype="S", delimiter=',', usecols=(1,), unpack=True)

for txt in names:
    print(txt.decode("utf-8"))
```

以下是執行結果:
```
王小明
陳小華
劉小杰
  .
  .
  .
周小花  
```

## 讀取多個欄位資料

在 numpy.genfromtxt() 中, 使用 dtype 參數指定取出的欄位名稱及型態, 另以 usecols 參數指定相對的欄位編號, 
即可取出特定多個欄位. 以下是一個例子:

```javascript
import numpy
scores=numpy.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

print(scores['chi'])
print(type(scores['chi']))
```

以下是執行結果:
```
[46 48 50 .... 35]
<class 'numpy.ndarray'> 
```

以下是一個中文欄位的例子:

```javascript
import numpy as np
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S20'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

# utf8編碼中文
name_utf8=[]

for n in scores['name']:
    name_utf8.append(n.decode('utf-8'))

print(name_utf8)
```

以下是執行結果:
```
['王小明', '陳小華', '劉小杰', ... , '周小花']
```
