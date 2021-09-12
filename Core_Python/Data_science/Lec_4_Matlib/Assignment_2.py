#Q.2
import matplotlib.pyplot as plt
import numpy as np
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
d={"venue":max_venue,
   "No._of_mathces": max_venue_value}

df1=pd.DataFrame([d])

df1.plot.bar(x='venue',y='No._of_mathces',color='red',fontsize=18)
plt.show()

plt.plot(max_venue,max_venue_value,'b*')
plt.show()

'''2nd method

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

'''df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':2,
    'num_pets':3
})
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.show()'''