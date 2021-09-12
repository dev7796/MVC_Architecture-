n = int(input("enter number of elements for List 1"))
lst = []
ls1=[]
ls3=[]
ls4=[]
ls5=[]
for i in range(n):
    elements = int(input("enter elements"))

    lst.append(elements)

m = int(input("enter number of elements for List 2"))

for i in range(m):
    elements = int(input("enter elements"))
    ls1.append(elements)

result=''
for element in lst:
    result += str(element)
    int(result)
print(result)

result1=''
for elements in ls1:
    result1 += str(elements)
    int(result1)
print(result1)

addition=int(result)+int(result1)
print(addition)
addition1=str(addition)
'''
addition1=str(addition)
ls4=addition1.split(',')
'''
multiply=int(result)*int(result1)
multiply1=str(multiply)
print(multiply)
lenadd=len(addition1)
for i in addition1:
    x=int(i)
    ls4.append(x)
print(ls4)
for i in multiply1 :
    x=int(i)
    ls5.append(x)
print(ls5)