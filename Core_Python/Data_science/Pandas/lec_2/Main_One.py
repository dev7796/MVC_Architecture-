import pandas as pd
import pymysql

df = pd.read_excel('writeExcel1.xls')
print("::: pd.read_excel() example::: \n")
print(df)

df.to_excel("writeExcel.xls")

df = pd.read_csv('readCSV.csv')
print('"::: pd.read_csv() example::: \n')
print(df)

df.to_csv('writeCSV.csv')

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb',
    cursorclass=pymysql.cursors.DictCursor
)

df = pd.read_sql('select * from loginmaster', connection)
df1 = pd.read_sql_query('select * from loginmaster', connection)
print("::: pd.read_sql() example::: \n")
print(df, "\n")
print(df1)

cursor1 = connection.cursor()
cursor1.execute("select * from loginmaster")
searchData = cursor1.fetchall()
print("searchData:::", searchData)

df = pd.read_sql('select * from loginmaster', connection)
print(df)

df.to_sql(name='loginmaster', con=connection, if_exists='append', index=False, chunksize=1000)
'''
cursor1 = connection.cursor()
print(cursor1.execute("select * from loginmaster").fetchall())

cursor1 = connection.cursor()
cursor1.execute("select * from loginmaster")
searchData = cursor1.fetchall()
print("searchData:::", searchData)

dataJSON = json.dumps(searchData)
df = pd.read_json(dataJSON)
print("::: pd.read_json() example::: \n")
print(df)
df.to_json('writeJson.json')
'''
