import numpy as np
import pandas as pd

# Series (list)
ls1 = ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 33.4, 66.7, 12.3]
df = pd.Series(ls1)
print(df)

# to create date as a index
dict = {'num_legs': [2, 4, 8, 0], 'num_wings': [2, 0, 0, 0], 'num_specimen_seen': [10, 2, 1, 8]}
df1 = pd.DataFrame(dict)
print(df1)
print(df1.shape)
df.index = pd.date_range(start='2019/2/1', periods=df.shape[0])
print(df.index)
df1.index = pd.date_range(start='2019/2/1', periods=df1.shape[0])
print(df1.index)

d1 = {'s1': [1, 2, 3, 4], 's2': [4, 5, 6, 7]}
df3 = pd.DataFrame(d1, index=df1.index)
print(df3)

# random generate float values
print(pd.DataFrame(np.random.rand(20, 5)))  # generate 20 rows and 5 columns of random floats num
