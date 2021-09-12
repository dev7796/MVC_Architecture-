import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb'
)

df1 = pd.read_sql('select * from loginmaster', connection)
print(df1)

connection1 = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb'
)

df2 = pd.read_sql('select * from loginmaster', connection1)
print(df2)

# append data at the end of df1
# display first all rows of df1 and then append rows of df2
print(df1.append(df2))

# # sql - join
# print(df1.join(df2, how='inner'))
# print(df1.join(df2, how='left'))

# Series concatenation
ls1 = [1, 2, 3, 4, 5, 6]
ls2 = ['a', 'b', 'c', 'd', 'e', 'f']
d1 = pd.Series(ls1)
d2 = pd.Series(ls2)
# print(d1,d2)
# print(pd.concat([d1,d2]))
# print(pd.concat([d1,d2], ignore_index=True))
print(pd.concat([d1, d2], keys=['s1', 's2']))

# Dataframe concatenation
df3 = pd.DataFrame(df1)
print(df3)
df4 = pd.DataFrame(df2)
print(df4)
print(pd.concat([df3, df4]))  # both print give same result
print(pd.concat([df1, df2]))  # both print give same result
