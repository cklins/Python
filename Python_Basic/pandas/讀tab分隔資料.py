import pandas as pd
import numpy as np


# 讀入資料, pandas.DataFrame
df=pd.read_csv('testSet-NOT-linearSeparable.txt', 
	sep='\t', 
	names=['feature01', 'feature02', 'label'])

print(df)
print('-'*30)


# 將 pandas.DataFrame 轉成 numpy.ndarray
x=df.as_matrix()
print(x)
print(x[:,2].astype(int))
print(type(x))
print('-'*30)
