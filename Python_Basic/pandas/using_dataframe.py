#======================================================
# 使用UCI資料集中的student-mat.csv資料(共395筆資料),
#======================================================
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold



#====================================================
# 讀入資料, pandas.DataFrame
#====================================================
df=pd.read_csv('student-mat.csv', 
	sep=';', 
	names=['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3'])

# 選擇若干特徵
#df_feature=df[['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']]
#df_feature=df[['G1', 'G2']]
#df_feature=df[['Medu','studytime', 'goout', 'health', 'absences', 'G1', 'G2']]
#df_feature=df[['Medu','studytime', 'goout', 'health', 'absences']]
#df_feature=df[['sex', 'address']]
#df_feature=df[['school']]
#df_feature=df[['Mjob']]
# 選擇標籤欄位
df_label=df[['G3']]
#----------------------------------------------------

print('原始資料')
print('='*30)
print(df)


#------------------------------------
# 更改/新增欄位內容
#------------------------------------
for col, col_data in df.iteritems():
	if col=='sex':
		col_data=col_data.replace(["M", "F"], ["男", "女"])
		df[col]=col_data       #更改
		df['gender']=col_data  #新增
		
print('更新後資料')
print('='*30)
print(df)		

		
#------------------------------------
# 刪除欄位內容
#------------------------------------		
del df['gender']
		
print('更新後資料')
print('='*30)
print(df)


#------------------------------------
# 建立一個新表格
#------------------------------------	
df2 = pd.DataFrame(columns=('gender', 'age'))
df2['gender']=df['sex']
df2['age']=df['age']

print('更新後資料')
print('='*30)
print(df2)


#------------------------------------
# 選擇某些條件的rows
#------------------------------------
df.set_index("sex", inplace=True)
df3=df.loc['男']
df3=df3.reset_index()

print('選取後資料')
print('='*30)
print(df3)
		
		
#====================================================
# k fold
# 將資料分成 training set 及 testing set
#====================================================
kf = KFold(n_splits=2, shuffle=True)
train_index, test_index = kf.split(df, df_label)
print('訓練資料索引')
print('='*30)
print(train_index)


# 訓練資料集:
# 訓練特徵: training_df_feature
# 訓練標籤: training_df_label
training_df_feature = df.iloc[train_index[0]]
training_df_label = df_label.iloc[train_index[0]]

print('訓練資料')
print('='*30)
print(training_df_feature)

print('訓練資料標籤')
print('='*30)
print(training_df_label)

# 測試資料集
# 測試特徵: testing_df_feature
# 測試標籤: testing_df_label
testing_df_feature = df.iloc[train_index[1]]
testing_df_label = df_label.iloc[train_index[1]]

print('測試資料')
print('='*30)
print(testing_df_feature)

print('測試資料標籤')
print('='*30)
print(testing_df_label)


testing_df_label_nparray = testing_df_label.as_matrix()
testing_df_label_nparray = testing_df_label_nparray.reshape(1, testing_df_label_nparray.shape[0])[0]	

print('測試資料標籤尺寸轉換')
print('='*30)
print(testing_df_label_nparray)	


	
