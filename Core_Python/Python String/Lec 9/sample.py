file = open("one.txt", "w+")
file1 = open("two.txt", "w+")
file3 = open("Agrade", "w+")
file4 = open("Bgrade", "w+")
file5 = open("Cgrade", "w+")
namelist = []
avg=[]
total=[]


def fn1():
    number = int(input("Enter Number Of Students"))

    for i in range(number):
        rollNo = int(input("Enter Rollno of studetns"))
        name = input("Enter Name Of The Students")

        s = str(rollNo)
        file.write(s)
        file.write(" - ")
        file.write(name)
        file.write('\n')
        marks = int(input("Enter Marks Of 1st subject"))
        marks1 = int(input("Enter Marks Of 2nd subject"))
        marks2 = int(input("Enter Marks Of 3rd subject"))
        m = str(marks)
        m1 = str(marks1)
        m2 = str(marks2)
        file1.write(s)
        file1.write(" - ")
        file1.write(m)
        file1.write(" - ")
        file1.write(m1)
        file1.write(" - ")
        file1.write(m2)
        file1.write('\n')


def fn2():
    #str1 = file.read()
    #str2 = file1.read()
    file1.seek(0, 0)
    file.seek(0, 0)
    for i in file:
        name = 0
        x1 = i.rstrip()
        x = x1.split(' ')
        namelist.append(x[-1])
        print(x)
'''

def fn3():
    '''
    str1=file1.read()
    str2=''.join(i for i in str1 if i.isdigit())
    ls1=list(str2)
    str2=ls1[1]+ls1[2]+ls1[3]
    ls3=list(str2)
    print(ls3)
    str3 = ls1[5] + ls1[6] + ls1[7]
    ls4 = list(str3)
    print(ls4)
    for i in range(0, len(ls3)):
        ls3[i] = int(ls3[i])
    sum = 0
    for i in range(0, len(ls4)):
        ls4[i] = int(ls4[i])
    sum1 = 0
    for t in ls3:
        sum1 = sum1+ t
    avg2 = sum1 / len(ls3)
    print(avg2)
    for t in ls4:
        sum = sum + t
    avg1 = sum / len(ls4)
    print(avg1)
    fn4(avg1,avg2)
'''

    for i in total:
        x = i.split(" ")
        avg1=int(x[-1])/3
        x.pop(-1)
        x.append(avg1)
        avg.append(x)

def fn4():
    avg.sort(key=lambda x:x[4])
    avg.reverse()
    print(avg)
    j = 0
    for i in avg:
        if avg[j][-1] >= 80:
            file3.write(avg[j][0]+" - "+avg[j][2]+" - "+str(avg[j][4]))
            file3.write("\n")
            j = j + 1
        elif 79 >= avg[j][-1] >= 60:
            file4.write(avg[j][0]+" - "+avg[j][2]+" - "+str(avg[j][4]))
            file3.write("\n")
            j = j + 1
        elif 59 >= avg[j][-1] >= 40:
            file5.write(avg[j][0]+" - "+avg[j][2]+" - "+str(avg[j][4]))
            file3.write("\n")
            j = j + 1




fn1()
fn2()
fn3()
fn4()


#def fn4(arg1):


'''

