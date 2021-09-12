from collections import OrderedDict

import numpy as np
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
# print(df)

# return rows where loginId > value
print(df[df['loginId'] > 3])

# rows where  loginId >value and loginId>value
print(df[(df['loginId'] > 3) & (df['loginId'] < 6)])

# sort by columnName in ascending order
print(df.sort_values('loginUsername'))

# sort by columnName in descending order
print(df.sort_values('loginUsername', ascending=False))

# sort values by loginId in descending order and username in ascending order
print(df.sort_values(['loginId', 'loginUsername'], ascending=[False, True]))

# group by columnName and return groupby object
obj = df.groupby('loginStatus')
print(obj.first())  # grouping based on status value(return first row)
print(obj.get_group('active'))  # grouping whose value is Activate
print(obj.get_group('deactive'))  # grouping whose value is Blocked

# group by multipal columnName and return groupby object
obj = df.groupby(['loginRole', 'loginStatus'])
print(obj.first())

obj = df.groupby('loginStatus')
print(obj.get_group('active'))
print(np.mean(obj.get_group('active')))
print(np.sum(obj.get_group('active')))

# Pivottable
table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item1', 'Item1']),
    ('CType', ['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD', ['1$', '2$', '3$', '4$']),
    ('EU', ['1€', '2€', '3€', '4€'])
))
d = pd.DataFrame(table)
print(d)
print(d.pivot(index='Item', columns='CType', values='USD'))

# group by status(Activate and Blocked value) and find mean
obj1 = df.groupby('loginStatus')
print((obj1.get_group('active')).mean())
print((obj1.get_group('deactive')).mean())

# apply function on dataframe

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df, "\n")
print(df.apply(np.mean), '\n')
print(df.apply(np.sqrt), '\n')
print(df.apply(np.sum, axis=0), '\n')  # sum of rowwise or index (default vale of axis=0)
print(df.apply(np.sum, axis=1), '\n')  # sum of columnwise
