studentInfo = open("studentInfo.txt", "w+")

studentMarks = open("studentMarks.txt", "w+")

aGrade = open("AGrade.txt", "w+")

bGrade = open("BGrade.txt", "w+")

cGrade = open("CGrade.txt", "w+")


def fn1(nostu):
    for i in range(nostu):

        rollno = input("Enter Roll No=")

        name = input("Enter Name=")

        studentInfo.write(rollno + "-" + name + "\n")

        studentMarks.write(rollno)

        for j in range(3):
            marks = input("Enter marks of student:")

            studentMarks.write("-" + marks)

        studentMarks.write("\n")


def fn2():
    studentInfo.seek(0, 0)

    studentMarks.seek(0, 0)

    ls1 = studentInfo.readlines()

    ls2 = studentMarks.readlines()

    print(ls1, ls2)

    return ls1, ls2


def fn3(ls1, ls2):
    ls3 = []
    ls4 = []

    for i in ls1:
        dummy = i.replace("\n", "")

        templs = dummy.split("-")

        ls3.append(templs)

    for j in ls2:
        dummy = j.replace("\n", "")

        templs = dummy.split("-")

        avg = (int(templs[1]) + int(templs[2]) + int(templs[3])) // 3

        ls4.append([templs[0], str(avg)])

    print(ls3, ls4)

    return ls3, ls4


def fn4(ls3, ls4):
    ls5 = []

    averageSet = {0}

    for i in ls3:

        for j in ls4:

            if i[0] == j[0]:
                dummy = i[0] + "-" + i[1] + "-" + j[1]

                averageSet.add(int(j[1]))

                ls5.append(dummy.split("-"))

    sortedList = list(averageSet)

    sortedList.sort(reverse=True)

    print(averageSet)

    print(sortedList)

    print(ls5)

    for i in sortedList:

        for j in ls5:

            if int(j[2]) == i and 80 < int(j[2]) <= 100:

                aGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")

            elif int(j[2]) == i and 60 < int(j[2]) <= 80:

                bGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")

            elif int(j[2]) == i and 40 < int(j[2]) <= 60:

                cGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")


nostu = int(input("Enter No. Of students:"))

fn1(nostu)

ls1, ls2 = fn2()

ls3, ls4 = fn3(ls1, ls2)

fn4(ls3, ls4)

studentInfo.close()

studentMarks.close()
