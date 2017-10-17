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

以下的例子由 scores.csv 讀入國文及英文成績, 並以此兩成績為 x軸 及 y軸, 顯示一個分數的散佈圖. 

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 讀入資料
df=pd.read_csv('scores.csv', 
	sep=',', 
	names=['id', 'names', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'lec'])
	
# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 待繪製的資料
chi=df['chi']
eng=df['eng']

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('國文-英文 成績關係圖')

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
plt.plot(chi, eng, 'ro')
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-1.png)



## 性別分類(1,2 -> 男,女) 

以下的例子由 scores.csv 讀入性別及英文成績, 並以此兩成績為 x軸 及 y軸, 顯示一個分數的散佈圖.
在原資料中, 性別內容為「1」及「2」, 但顯示時將標籤轉換為「男」及「女」.

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 讀入資料
df=pd.read_csv('scores.csv', 
    sep=',', 
    names=['id', 'names', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'lec'])
	
# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 待繪製的資料
eng=df['eng']
gender=df['gender']

# 性別資料(1,2)及顯示標籤(男, 女)
x=[1, 2]  #在scores.csv中, 男:1, 女:2
labels = ['男', '女']

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('性別-成績 關係圖')

# 設定x軸及y軸標題
plt.xlabel('性別')
plt.ylabel('英文成績')

# 性別資料轉換為顯示標籤
plt.xticks(x, labels)

# 設定圖邊界
plt.margins(0.4)
plt.subplots_adjust(bottom=0.15)

# 資料表內的grid虛線
ax.grid(which='both')
ax.grid(which='minor', alpha=0.5)
ax.grid(which='major', alpha=0.8)

# 繪製圖
plt.plot(gender, eng, 'mx')
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-2.png)



## 成績人數計數 

以下的例子由 scores.csv 讀入英文成績, 程式累計各分數之人數, 並以此成績及人數為 x軸 及 y軸, 顯示一個分數/人數的的bar圖.

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 讀入資料
df=pd.read_csv('scores.csv', 
    sep=',', 
    names=['id', 'names', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'lec'])
	
# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 待繪製的資料
eng=df['eng']

# 整理待繪製的資料
eng_count = np.bincount(eng)          #計算各個成績有多少人同分
eng_person = eng_count[eng_count>0]    #統計人數>0的人數
eng_score = np.nonzero(eng_count)[0]   #統計人數>0的分數

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('英文成績-人數 關係圖')

# 設定x軸及y軸標題
plt.xlabel('英文成績')
plt.ylabel('人數')

# 設定圖邊界
plt.margins(0.05)
plt.subplots_adjust(bottom=0.1)

# 資料表內的grid虛線
ax.grid(which='both')
ax.grid(which='minor', alpha=0.5)
ax.grid(which='major', alpha=0.8)

# 設定x軸資料bar顯示值
plt.xticks(eng_score + 0.5, tuple(eng_score))

# 繪製圖
plt.bar(eng_score, eng_person)
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-3.png)


## 各科成績的 box-plot 圖 

以下的例子由 scores.csv 讀入國文, 英文, 數學, 社會, 自然等五科成績, 以 box-plot 表現最小值, 最大值, 上四分位數, 下四分位數及中位數.

```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 讀入資料
df=pd.read_csv('scores.csv', 
    sep=',', 
    names=['id', 'names', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'lec'])

# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 待繪製的資料
chi=df['chi']
eng=df['eng']
mat=df['mat']
soc=df['soc']
nat=df['nat']
all_data = [chi, eng, mat, soc, nat]

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('各科成績的 box-plot 圖')

# 設定x軸及y軸標題
plt.xlabel('科目')
plt.ylabel('成績')

# 設定圖邊界
plt.margins(0.05)
plt.subplots_adjust(bottom=0.1)

# 資料表內的grid虛線
ax.grid(which='both')
ax.grid(which='minor', alpha=0.5)
ax.grid(which='major', alpha=0.8)

# 資料表內的grid水平虛線
ax.yaxis.grid(True)
ax.set_xticks([y+1 for y in range(len(all_data))])

# 建立 box plot
ax.boxplot(all_data)

# 繪製圖
plt.setp(ax, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['國文', '英文', '數學', '社會', '自然'])
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-4.png)
