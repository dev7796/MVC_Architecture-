Student = {'s1':{'rollno':int(input("enter rollno")),'name':input("enter name"),'marks':int(input("enter marks")),'grade':None},

's2':{'rollno':int(input("enter rollno")),'name':input("enter name"),'marks':int(input("enter marks")),'grade':None},

's3':{'rollno':int(input("enter rollno")),'name':input("enter name"),'marks':int(input("enter marks")),'grade':None}
        }

for i,j in Student.items():

    for a,b in j.items():

        if a == 'marks':
            if 80<b<100:
                j['grade']='A'
            else:
                j['grade']='B'

print(Student)
