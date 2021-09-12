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
print(df)

# Rename column
df.columns = ['loginId', 'loginUsename', 'loginPassword', 'loginRole', 'loginStatus']
print(df)

# check for null values and return boolean array
# isnull then return true otherwise return false
print(pd.isnull(df))

# opposite to isnull()
# notnull then return True otherwise return false

print(pd.notnull(df))

# drop all rows that contain null value
print(df.dropna())

# drop all columns that contain null value
# axis = 0 means row and axis = 1 means column
print(df.dropna(axis=1))

# thresh is threshold value
print(df.dropna(axis=1, thresh=7))

# replace all null value with x
print(df.fillna('xx'))

# replace all null value with mean value
print(df.fillna(int(df.mean())))

# convert into float type but need input in dataframe(df) type
print(df['loginId'].astype(float))

# replace all old value with new new value
print(df['loginRole'].replace('user', 'ROLE_USER'))
print(df['loginStatus'].replace('deactive', 'block'))

# replace multipal values
print(df['loginStatus'].replace(['block', 'unblock', None], ['deactive', 'active', 'null']))

# rename of selective columns
print(df.rename(columns={'loginId': 'login_Id',
                         'loginUsename': 'login_Usename',
                         'loginPassword': 'login_Password',
                         'loginRole': 'login_Role',
                         'loginStatus': 'login_Status'}))

# selective renamining of index
print(df.rename(index=lambda x: x + 1))
print(df.rename(index=lambda x: x + 2))

# selective renameing of columns
print(df.rename(columns=lambda x: x + '{}'.format(1)))
