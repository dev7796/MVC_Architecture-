import pandas as pd

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb',
    cursorclass=pymysql.cursors.DictCursor
)

data = pd.read_sql_query('select * from loginmaster', connection)
print("data::")
print(data)

data1 = pd.DataFrame(data, columns=['loginId', 'loginUsername', 'loginPassword', 'loginRole', 'loginStatus'])
print("data1::")
print(data1)

print("\n Find max value using pandas::")
print(data1['loginId'].max())
