import pandas as pd
import xlwt
df = pd.read_csv('titanic.csv')
print("::: pd.read_excel() example::: \n")
print(df)
#to see first 8 rows of dataframe
#if not provided anything it returns 5 rows by default
print(df.head(8))
#to get last n rows use tail function
print(df.tail(10))
#to check the datatypes

print(df.dtypes)
#to convert file to xls and also removing index with giving sheet name
df.to_excel('titanic.xls', sheet_name='passengers', index=False)
#for technical summary
df.info()
#df.to_excel("titanic.xls")



'''
df = pd.read_csv('readCSV.csv')
print('"::: pd.read_csv() example::: \n')
print(df)

df.to_csv('writeCSV.csv')'''

