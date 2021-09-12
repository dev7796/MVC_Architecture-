import json

import pandas as pd
import pymysql

ls = ['aa', 'bb', 'cc', 'dd', 1, 2, 3, 4, 5, 33.4, 66.7, 12.3]
# ls1 = [1,2,3,4,5,6,7,8,9,10,11,12]
ls1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
data = pd.Series(ls, index=ls1)  # default index start with 0
print("::: pd.Series() example::: \n")
print(data)

dict = {'num_legs': [2, 4, 8, 0], 'num_wings': [2, 0, 0, 0], 'num_specimen_seen': [10, 2, 1, 8]}
index = ['falcon', 'dog', 'spider', 'fish']
data = pd.DataFrame(dict, index=index)  # default index start with 0
print("::: pd.DataFrame() example::: \n")
print(data)
data.to_excel("writeExcel.xls")

data1 = pd.read_excel('writeExcel.xls')
print("::: pd.read_excel() example::: \n")
print(data1)

print(pd.read_clipboard())

ls1 = ['a', 'b', 'c', 'd', 'e']
data = pd.read_csv('../../../../Downloads/Sample1.csv')
print("::: pd.read_csv() example::: \n")
print(data)

data = pd.read_table('Sample2.txt', sep='\t')
print("::: pd.read_table() example::: \n")
print(data)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb',
    cursorclass=pymysql.cursors.DictCursor
)
data = pd.read_sql_query('select * from loginmaster', connection)
print("::: pd.read_sql_query() example::: \n")
print(data)

cursor1 = connection.cursor()
cursor1.execute('select * from loginmaster')
searchData = cursor1.fetchall()

jsn = json.dumps(searchData)
print("jsn:::", jsn)
print()

data1 = pd.read_json(jsn)
print(":::pd.read_json() example::: \n")
print(data1)

print()
