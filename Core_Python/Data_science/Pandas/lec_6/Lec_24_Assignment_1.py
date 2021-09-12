import pandas as pd
import pymysql as sql
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user='root',
                               pw='gladiators',
                               db='Lec_24'))
marks1={}
marks2={}
spi={}
cpi={}
a,b,c=[],[],[]
number=int(input("Enter No. of Student: "))
for s in range(number):
    enrollment_number=int(input("Enter Enrollment Number: "))
    name=input("Enter Student Name: ")
    gender=input("Enter Student Gender: ")
    email=input("Enter Student Email: ")
    contact=int(input("Enter Student Contact Info: "))
    a.append([enrollment_number,name,gender,email,contact])
    no_of_semesters=int(input("Enter No. of Semester: "))
    for i in range(no_of_semesters):
        #no_of_subjects=int(input("Enter number of subjects in sem:"+str(i+1)+" "))
        print("Sem"+str(i+1)+":")
        marks1[i+1]=int(input("Enter Marks For Subjects1: "))
        marks2[i+1]=int(input("Enter Marks For Subjects2: "))
        spi[i+1]=float(input("Enter spi for sem:"+str(i+1)+" "))
        cpi[i+1]=float(input("Enter CPI for sem:"+str(i+1)+" "))
    b.append(list(marks1.values())+list(marks2.values())+list(spi.values())+list(cpi.values()))
    for o in range(len(b[s]),32):
            b[s].append(0)

array=[['Sem1','Sem1','Sem2','Sem2','Sem3','Sem3','Sem4','Sem4','Sem5','Sem5','Sem6','Sem6','Sem7','Sem7','Sem8','Sem8','Sem1','Sem1','Sem2','Sem2','Sem3','Sem3','Sem4','Sem4','Sem5','Sem5','Sem6','Sem6','Sem7','Sem7','Sem8','Sem8'],
        ['Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Sub1','Sub2','Spi','Cpi','Spi','Cpi','Spi','Cpi','Spi','Cpi','Spi','Cpi','Spi','Cpi','Spi','Cpi','Spi','Cpi']]
tuples = list(zip(*array))
Semester_values = pd.MultiIndex.from_tuples(tuples)
df = pd.DataFrame(a,columns=['enrollment_number','Name','gender','email','contact'])
df_sem = pd.DataFrame(b,columns=Semester_values)
df_combine = pd.concat([df,df_sem],axis=1)
print(df_combine)
df_combine.to_sql('StudentData', con=engine, if_exists='append')
