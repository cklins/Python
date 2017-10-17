# 用 matplotlib 顯示圖表 


```
import numpy as np
import matplotlib.pyplot as plt

# 定義函式
def fx01(x):
    return np.sin(x)
	
def fx02(x):
    return np.cos(x)	

# 產生角度資料
x=np.arange(0, 10, 0.05) 

# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 設定圖標題
plt.title('角度及sin(), cos()函數值')

# 設定x軸及y軸標題
plt.xlabel('角度')
plt.ylabel('三角函數值')

# 資料表內的grid
plt.grid(True)

# 繪製資料
plt.plot(x, fx01(x), 'r-', x, fx02(x), 'b--')

# 設定資料說明
plt.legend(['sin(x)', 'cos(x)'], numpoints=1, loc='lower left')

# 顯示圖表
plt.show()
```

以下是執行結果:<p>
![GitHub Logo](/images/fig7-7.jpg)
