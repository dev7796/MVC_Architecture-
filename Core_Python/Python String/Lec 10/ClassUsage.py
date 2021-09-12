from Task_1 import *

Namels = []
rollls = []
m1ls = []
m2ls = []
m3ls = []
totalmarks = []


class studentInfo:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        '''Namels.append(name)
        rollls.append(rollno)
        print(Namels,rollls)'''


class studentMarks:
    def __init__(self, rollno, m1, m2, m3):
        self.rollno = rollno
        m2ls.append(self.rollno)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

def average():
    p=0
    for i in m1ls:
        sumation = sum(i)
        avg = sumation // 3
        m3ls.append([m2ls[p], avg])
        p=p+1
    print("Roll no list", m3ls)

    ''' totl = 0
            for i in range(len(x)):
                totl += int(x[i])
            totalmarks.append(x[0] + str(totl))
            '''


class main:
    num = int(input("Enter Number of Students"))
    for i in range(num):
        rollno = int(input("Enter Roll No= "))
        name = input("Enter name= ")
        studentinfo = studentInfo(rollno, name)
        Namels.append([rollno, name])

        m1 = int(input("Enter marks1="))
        m2 = int(input("Enter marks2="))
        m3 = int(input("Enter marks3="))
        m1ls.append([m1, m2, m3])
        studentmarks = studentMarks(rollno, m1, m2, m3)

    print(Namels)
    average()
    fn4(Namels, m3ls)
