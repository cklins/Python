# 用 matplotlib 顯示圖表 

## 準備 CSV 格式檔案

以下是一個 csv 格式資料, 每列代表一個學生的成績資料, 一個成績資料項目間以逗號隔開.
其項目意義分別為「序號」,「姓名」,「性別」,「國文」,「英文」,「數學」,「社會」,「自然」及「寫作」.
<p>
資料檔名稱為「scores.csv」, 和 Python 測試程式放在同一個資料夾中.

```
1,王小明,1,46,56,42,48,37,10
2,陳小華,1,48,51,39,48,43,10
3,劉小杰,1,50,52,47,41,42,8
  .
  .
  .
402,周小花,2,35,35,48,27,28,8
```

## 散佈圖 

以下的例子由 scores.csv 讀入國文及英文成績, 並以此兩成績為 x軸 及 y軸, 顯示一個分數的散佈圖,
以不同顏色分別不同性別. 

```
import numpy as np
import matplotlib.pyplot as plt

# 讀入資料
scores=np.genfromtxt('scores.csv',  dtype=[('id', 'i'), ('name', 'S'), ('gender', 'i'), ('chi', 'i'), ('eng', 'i'), ('mat', 'i'), ('soc', 'i'), ('nat', 'i'), ('lec', 'i')], delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8,), unpack=True)

# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 待繪製的資料
male=(scores['gender']==1)
female=(scores['gender']==2)

chi=scores['chi']          #男生的成績
chi_male=chi[male]
chi_female=chi[female]

eng=scores['eng']         #女生的成績
eng_male=eng[male]
eng_female=eng[female]

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('國文-英文 性別分類成績圖')

# 設定x軸及y軸標題
plt.xlabel('國文成績')
plt.ylabel('英文成績')

# 設定圖邊界
plt.margins(0.4)
plt.subplots_adjust(bottom=0.15)

# 資料表內的grid虛線
ax.grid(which='both')
ax.grid(which='minor', alpha=0.5)
ax.grid(which='major', alpha=0.8)

# 設定x軸及y軸的尺規範圍
plt.axis([20, 70, 10, 65])

#藍色:'b'      |  綠色: 'g'     |  紅色: 'r'     |  藍綠色:'c'    |  紅紫色:'m'   |  黃色:'y'         |  黑色:'k'    |  白色:'w'
#實線:'-'      |  虛線: '--'    |  虛點線:'-.'   |  點線:':'      |  點:'.'       |
#圓形:'o'      |  上三角:'^'    |  下三角:'v'    |  左三角:'<'    |  右三角:'>'   |  方形:'s'         |  加號:'+'    |  叉形:'x'     |  棱形:'D'  |   細棱形:'d'
#三腳朝下:'1'  |  三腳朝上:'2'  |  三腳朝左:'3'  |  三腳朝右:'4'  |  六角形:'h'   |  旋轉六角形:'H'   |  五角形:'p'  |  垂直線:'|'

# 繪製圖
plt.plot(chi_male, eng_male, 'go')      #男生資料
plt.plot(chi_female, eng_female, 'rx')  #女生資料
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-5.png)

