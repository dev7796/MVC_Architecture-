import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb',
    cursorclass=pymysql.cursors.DictCursor
)

df = pd.read_sql('select * from loginmaster', connection)
print(df,"\n")


print(df.describe())

print(df['loginId'].mean())

print(df.corr)
print(df['loginId'].corr)

print(df.count())

print(df['loginId'].max())

print(df['loginId'].min())

print(df['loginId'].median())

print(df['loginId'].std())
