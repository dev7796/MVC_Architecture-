n1 = int(input())
n2 = int(input())

ls1 = []
ls2 = []

str1 = ""

str2 = ""

for i in range(n1):
    ls1.append(int(input()))
    str1 = str1 + str(ls1[i])

for j in range(n2):
    ls2.append(int(input()))
    str2 = str2 + str(ls2[j])

print(ls1)
print(ls2)

add = str(int(str1) + int(str2))
mul = str(int(str1) * int(str2))

ls3 = [int(a) for a in add]
ls4 = [int(b) for b in mul]

print(ls3)
print(ls4)
