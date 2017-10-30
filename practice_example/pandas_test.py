import pandas as pd
import numpy as np

# plotly demo
import plotly.plotly as py
import plotly.figure_factory as ff

plotly.tools.set_credentials_file(username='cklin', api_key='jO4F8Th8jjTAXIe0q3tl')

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

table = ff.create_table(data_matrix)
py.iplot(table, filename='simple_table')


# 1 pandas 基本介绍
s = pd.Series([1,3,6,np.nan,4,1]) # similar with 1D numpy
print(s)
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
print(df['B'])
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
print(df2)
print(df2.dtypes)

print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))


# 2 选择数据

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102', ['A','B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

# mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 0])

