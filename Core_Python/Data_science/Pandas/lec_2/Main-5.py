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

print(df, "\n")

# return result as a Series
print(df['loginUsername'])

# return result as Dataframe
print(df[['loginUsername', 'loginPassword']])

# selection by passing position(start with 0 position(consider as index))
# (select based on index)
df = df.set_index(df['loginId'])
print("df::", df)

print(df.iloc[0], "\n")  # return first row data as a result

# select by passing index (start with)
# (select based on passed value)
df = df.set_index('loginId')
print(df.loc[2])

# first row
print(df.iloc[0])

# first element of first column
print(df.iloc[0, 0])

# first 3 rows
print(df.iloc[0:3])

# all rows of second column(username)
print(df.iloc[:, 1])

# first 3 rows of second column
print(df.iloc[0:3, 1])

# last row
print(df.iloc[-1])

# 3 rows of first two columns
print(df.iloc[0:3, 0:2])
