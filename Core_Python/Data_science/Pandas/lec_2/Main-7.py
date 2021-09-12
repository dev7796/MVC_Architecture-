import pandas as pd

'''
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb'

)

df = pd.read_sql('select * from loginmaster', connection)
print(df, "\n")

print(df.head(), "\n")  # if not pass n value as a parameter then it show first 5 rows as a result
print(df.head(3))  # shows first n rows as a result

print(df.tail(), "\n")  # if not pass n value as a parameter then it show last 5 rows as a result
print(df.tail(3), "\n")  # shows last n rows as a result

n1 = df.shape
print("rows and columns::", n1, "\n")

print("Table Information:: \n")
print(df.info())

# display count,mean,median,max alues for numeric columns
df1 = pd.read_sql('select * from loginmaster', connection)
print("Table description:: \n")
print(df1.describe())

# The resulting object will be in descending order so that the first element is the most frequently-occurring element.
# default value of sort is True and it Sort by values
# ascending is False
idx = pd.Index(['Harry', 'Mike', 'Arther', 'Nick', 'Harry', 'Arther'], name='Student')
idx = pd.Index([21, 10, 30, 40, 50, 10, 50])
print("idx::", idx, "\n")
print(idx.value_counts(dropna=False, ascending=True))
df1 = df['loginUsername']
print(df1.value_counts(dropna=False))

df = pd.DataFrame({'ID': ['1', '2', '3'], 'J1': [0, 2, 3], 'J2': [1, 4, 5]})
print(df, "\n")
lst = ['a', 'b', 'c', 'd', 'e', 'f']


def sublst(row):
    print(row['J1'], ":", row['J2'], "=", lst[row['J1']:row['J2']])
    return lst[row['J1']:row['J2']]


df['J3'] = df.apply(sublst, axis=1)
print(df)

'''
raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [32, 32, 32, 21],
            'favorite_color': ['blue', 'red', 'yellow', "green"],
            'grade': [88, 92, 95, 70]}
df = pd.DataFrame(raw_data, index=['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
print("before Sorting\n", df)
a = df.sort_values(['age', 'grade'], ascending=[True, False])
print("\nafter sorting:\n", a)
