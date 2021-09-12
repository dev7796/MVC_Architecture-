import pandas as pd

ls = [1,2,3,4,5,33.4,66.7,12.3,12,12,23,45]
#ls1 = [1,2,3,4,5,6,7,8,9,10,11,12]
ls1 = ['a','b','c','d','e','f','g','h','i','j','k','l']
data = pd.Series(ls,index=ls1) #default index start with 0
print("::: pd.Series() example::: \n")
print(data)
#returns max value
print(data.max())
#The describe() method provides a quick overview of the numerical data in a DataFram
print(data.describe())



dict = {'num_legs': [2, 4, 8, 0],'num_wings': [2, 0, 0, 0],'num_specimen_seen': [10, 2, 1, 8]}
index = ['falcon', 'dog', 'spider', 'fish']
data = pd.DataFrame(dict,index=index)   #default index start with 0
print("::: pd.DataFrame() example::: \n")
print(data)
#returns max value of num legs
print(data['num_legs'].max())




