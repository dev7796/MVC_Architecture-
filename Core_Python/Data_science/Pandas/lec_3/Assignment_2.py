#Q.2

import pandas as pd
import xlwt
import xlrd
import pymysql as sql
import numpy as np
data = pd.read_excel('IPL.xls')
df=pd.DataFrame(data,columns=['Venue'])
result={}
Unique_data=df['Venue'].unique()
for i in Unique_data:
    result[i]=df[df['Venue']==i].count().max()
v = list(result.values())
k = list(result.keys())
max_venue=k[v.index(max(v))]
max_venue_value=max(v)
d={"":[max_venue,max_venue_value]}
df1=pd.DataFrame(d,index=['Venue',"No. of Matches"])
print(df1)




'''
2nd method

df = pd.DataFrame(data, columns= ['Venue'])
lst=df['Venue'].to_list()
result={}
for letter in lst:
    # Check if the letter needs to be counted or not
    if letter not in result:
        result[letter] = 0
    # Add or increment the value in the dictionary
    result[letter] = result[letter] + 1
v = list(result.values())
k = list(result.keys())
max_venue=k[v.index(max(v))]
max_venue_value=max(v)
d={"":[max_venue,max_venue_value]}
df1=pd.DataFrame(d,index=['Venue',"No. of Matches"])
print(df1)
'''






'''
3rd method using database

connection = sql.connect(host='127.0.0.1',
                         user='root',
                         passwd='gladiators',
                         db='IPLData')

cursor = connection.cursor()
sql1= "CREATE TABLE `IPL` (`Venue` INT NOT NULL,`No._of_Mathces` INT NOT NULL);"
cursor.execute(sql1)

#max_key = max(result, key=result.get)
#print(max_key)
#df = pd.read_sql('SELECT * FROM IPL',connection)
sql2="INSERT INTO 'IPL'('Venue','No._of_Mathces') VALUES (%s,%s)"
cursor.execute(sql2,(max_venue,max_venue_value))
#sql_conn.commit()'''