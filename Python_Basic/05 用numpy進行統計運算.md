# 用 numpy 進行統計運算

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

## average, max, min, median, var 及 std

在 numpy 中, 提供 average(), max(), min(), median(), var() 及 std() 等統計函式, 可進行統計運算. 以下是一個例子:

```javascript
import numpy as np

scores=np.genfromtxt('scores.csv', dtype="i", delimiter=',', usecols=(3,), unpack=True)

print('平均=', np.mean(scores))
print('最大值=', np.max(scores))
print('最小值=', np.min(scores))
print('中位數=', np.median(scores))
print('變異數=', np.var(scores))
print('標準差=', np.std(scores))
```

以下是執行結果:
```
平均= 45.9626865672
最大值= 60
最小值= 25
中位數= 46.0
變異數= 30.2996027326
標準差= 5.50450749228  
```
