Nooflines = int(input("Enter Number of Lines"))
file = open("one.txt", "w+")
l1 = []
l2 = []
l3, l4 = [], []


def writing(lines):
    for i in range(lines):
        file.write(input("Enter lines") + '\n')


writing(Nooflines)
file.seek(0, 0)
position = file.tell()
print("Current Position of cursor", position)
i = 0
file1 = open("two.txt", "w+")


def reading():
    str = file.readlines()
    file1.writelines(str[::-1])


reading()
position = file.tell()
print("Current Position of cursor", position)

file1.seek(0, 0)
position = file1.tell()
print("Current Position of cursor", position)


def replace():
    word = input("Enter the word to replace")
    Word1 = input("Enter the word to be replaced with")
    str = file1.read()
    l2 = str.split('\n')
    for i in l2:
        l3.append(i.split(" "))
    for i in range(0, len(l3)):
        for j in l3[i]:
            if word in j:
                j = Word1
            l4.append(j)
    print(l4)
    for i in l4:
        t = t + i
    print(t)
replace()
"""if word in str:
        print("Yes the word is present and it will be replaced")

    for line in str:
        s=line.replace(word,Word1)
        l1.append(s)
    s=""

    for i in l1:
        s = s + i

    file2 = open("two.txt","w")
    file2.write(s)
"""

