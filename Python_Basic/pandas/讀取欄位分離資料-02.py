import matplotlib.pyplot as plt
import pandas as pd

# 讀入資料, data frame
df=pd.read_csv('scores.csv', encoding='big5', names=['serno', 'stuname', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'wri'], index_col='serno')
print(df)


# 整理資料
x=df['chi']
y=df['eng']

# 找出一條趨近測試資料的1階線性方程式

# 設定字型及大小
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.size'] = 14

# 設定圖標題
fig, ax = plt.subplots()
ax.set_title('成績分佈')

# 設定x軸及y軸標題
plt.xlabel('國文')
plt.ylabel('英文')

# 將測試資料畫在圖上
plt.scatter(x, y)

# 畫出格線
plt.grid()

# 顯示圖表
plt.show()