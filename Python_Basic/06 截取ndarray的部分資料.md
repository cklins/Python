# 截取 ndarray 的部分資料 

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

## 截取某段落資料

在 ndarray 中, 在中括號中加入起始及終止指標可截取某段落資料. 以下是一個例子:

```javascript
import numpy as np
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

# 排序
chi=np.msort(scores['chi'])

print(chi)

print('前10筆=', chi[:10])
print('後10筆=', chi[-10:])
print('第5-10筆(指標從0開始)=', chi[5:10])
```

以下是執行結果:
```
[25 27 29 31 31 32 32 34 35 35 35 .... 56 56 56 56 56 56 56 60 60 60 60]
前10筆= [25 27 29 31 31 32 32 34 35 35]
後10筆= [56 56 56 56 56 56 60 60 60 60]
第5-10筆(指標從0開始)= [32 32 34 35 35]
```

## 加入選取條件(1)

讓 ndarray 進行邏輯運算, 可得到一個大小與原 ndarray 相同的 ndarray, 其由 True 及 False 組成, 
可作為 ndarray 的 index, 如此只有相對為 True 的資料項目可被處理. 以下是一個例子:

```javascript
import numpy as np
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

chi=scores['chi']
hs=chi>50 # 結果是一個 ndarray, 如 [True, True, False, False, False, ....]

print(chi[hs])
print('平均=', np.mean(chi[hs]))
print('標準差=', np.std(chi[hs]))
```

以下是執行結果:
```
[56 53 53 53 53 53 53 53 .... 56 53 53 56 53]
平均= 54.1875
標準差= 1.97543507866
```


## 加入選取條件(2)

可用 numpy.where(), 加入條件後可得到一個 array, 其內容為 index. 
若將其作為另一 ndarray 的索引值, 只列出索引值相同的資料. 以下是一個例子:

```javascript
import numpy as np
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

chi=scores['chi']

hsi=np.where(chi>50)
print(hsi)
print(chi[hsi])
```

以下是執行結果:
```
(array([  8,  10,  24,  29,  .... 334, 353, 358, 389], dtype=int32),)
[56 53 53 53 .... 53 53 56 53]
```


## 加入選取條件(3)

numpy.where()中可加入且「&」及或「|」條件, 只列出索引值相同的資料. 以下是一個例子:

```javascript
import numpy as np
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 3, 4, 5, 6, 7, 8,), unpack=True)

hsi=np.where((scores['chi']>55) & (scores['eng']>55)) #國文及英文均>=55
print(hsi)

print('國文=', scores['chi'][hsi])
print('英文=', scores['eng'][hsi])
```

以下是執行結果:
```
(array([  8,  81,  97, 166, 272], dtype=int32),)
國文= [56 56 56 56 56]
英文= [60 60 60 56 56]
```