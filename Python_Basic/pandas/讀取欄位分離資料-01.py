import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd

# 讀入資料
df=pd.read_table('web_traffic.tsv', names=['time', 'amount'])

# 整理資料
df=df[~np.isnan(df['amount'])]
x=df['time']
y=df['amount']

# 找出一條趨近測試資料的1階線性方程式
fp1, residuals, rank, sv, rcond=sp.polyfit(x, y, 3, full=True)

# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('網路流量')

# 設定x軸及y軸標題
plt.xlabel('日期')
plt.ylabel('每小時用量')

# 線性方程式為 f1
f1=sp.poly1d(fp1)

#傳回1000個(從0到x元素個數), 間隔相同的數
fx=sp.linspace(0, len(x), 1000)

# 將產生的數一個個代入線性方程式, 並畫在圖上
plt.plot(fx, f1(fx), linewidth=4)

# 產生左上角的標籤說明
plt.legend(["趨近線性方程式"], loc="upper left")

# 將測試資料畫在圖上
plt.scatter(x, y)

# 畫出格線
plt.grid()

# 顯示圖表
plt.show()