from mysql.connector import MySQLConnection, Error
import pandas as pd
import matplotlib.pyplot as plt
import pymysql as sql
import numpy as np

connection = sql.connect(host='127.0.0.1',
                         user='root',
                         passwd='gladiators',
                         db='employee')

cursor = connection.cursor()
df = pd.read_sql('SELECT * FROM employers',connection)
print(df)

#to insert values into the database
'''sql1 = "INSERT INTO `employee`.`employers` (`employers_ID`, `username`, `password`, `time`, `age`) VALUES ('5', 'john', 'mulch', '34', '28');"
cursor.execute(sql1)
connection.commit()
print(df)
'''

#to select a particular value from the database
'''sql3="SELECT * FROM employers where employers_ID = 5"
cursor.execute(sql3)
res=cursor.fetchall()
for i in res:
    print(i)
connection.commit()'''

# to make a dataframe and to remove index
'''print(df[['employers_ID','age']])
df=df.set_index('employers_ID')
print(df)
print("*************")'''

'''df.index =pd.date_range('1900/1/30',periods=df.shape[0])
print(df)
#if the indexes are not integers we cannot use loc
print(df.loc[5])
print(df.iloc[5])
#some iloc functions
print(df.iloc[2,1])
print(df.iloc[:,1])
print(df.iloc[0:3,1])#0,1,2 rows with index 1 column
print(df.iloc[-1])#last row
print(df.iloc[0:3,0:3])'''

print(df.columns)
#to change the name of the columns
'''df.columns = ["employers_ID","username","password","time","day"]
print(df)'''

print(df.rename(columns={'age':'day'}))
print(df.rename_axis("animals"))#used to provide name to the axis

print(pd.isnull(df))
print(df["employers_ID"].astype(int))#to convert data type

#print(df['username'].replace('jay','JAY'))
#to change multiple values
print(df['username'].replace(['jay','gk','aash'],['JAY','GK','AASH']))

#print(df[df["username"]=='john' & df["username"]=='aash'])
print(df[(df['age'] > 20)& (df['employers_ID'] < 3)])
print(df.sort_values('username'))
print(df.sort_values(['age','password'],ascending=[False,True]))#doubt how does it work

'''x=df.groupby("age")["time"]
#only returns unique values
print("this is it",x.first())'''

#Find the average across all columns for every unique col1​ group
print("**********",df.groupby('age').agg(np.mean))

#print(df.apply(np.mean))

#print(df.apply(np.max,axis=1))

'''print(df.describe())#Summary statistics for numerical columns
print("this is mean",df.mean())
print("this is count",df.count())#Returns the number of non-null values in each DataFrame column
print("this is min",df.min())#Returns the lowest value in each column
print("this is std",df.std())
print("this is corr",df.corr())#Returns the correlation between columns in a DataFrame
print("this is max",df.max())
print("this is median",df.median())# Returns the median of each column'''


'''print(df.fillna('x'))
print("this is dropna",df.dropna(axis=0, thresh = 4))#Drop all columns have less than n non-null values
# axis=0 means rows and axis=1 means columns'''

#Replace all null values with the mean (mean can be replaced with
# almost any function from the statistics section)
print(df.fillna(df.mean()))

print(df.rename(index=lambda x: x + 1))#Mass renaming of index












