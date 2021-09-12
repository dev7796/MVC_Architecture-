import pymysql
import pymysql.cursors

database = pymysql.connect(
        user='root',
        password='gladiators',
        db='employee',
        cursorclass=pymysql.cursors.DictCursor
    )
c = database.cursor()

c.execute("SELECT username, password, age FROM employers")
employee = c.fetchall()

#print(employee['name'])
# Jim Biggs
#print(employee['position'])
# Programmer
#print(employee['age'])
# 35
print(employee)
ls=[]
ls1=[]
ls2=[]

for i in employee:
    for k,v in i.items():
        if k=='username':
            ls.append(v)
        elif k=='password':
            ls1.append([v])
        else:
            ls2.append(v)

print(ls,ls1)
