import pandas as pd

# 讀入資料, data frame
df=pd.read_csv('scores01.csv', encoding='big5', names=['serno', 'stuname', 'gender', 'chi', 'eng', 'mat', 'soc', 'nat', 'wri'], index_col='serno')

# 前10筆
print(df[:10])

# 第11~20筆
print(df[10:20])

# 只印某些 column
print(df['stuname'])
print(df['stuname'][:20])

# 只印某些 columns
print(df[['stuname', 'gender']])
print(df[['stuname', 'gender']][:20])

# 合併 merge
df2=pd.read_csv('scores02.csv', encoding='big5', names=['serno', 'stuname', 'gender', 'chi', 'eng', 'mat'], index_col='serno')
df3=pd.read_csv('scores03.csv', encoding='big5', names=['serno', 'stuname', 'gender', 'soc', 'nat', 'wri'], index_col='serno')
print('----merge--------------------------------------')
print(pd.merge(df2, df3))

# 連結 concat
print('----concat--------------------------------------')
df4=pd.concat([df2, df3])
print(df4)


# 輸出到檔案
df2.to_csv('test_out.csv')