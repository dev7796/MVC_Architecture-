n = input("enter number of values")
a = n.split(',')
b = len(a)
ls1=[]
ls2=[]

for i in a:
    if i.isdigit():
        ls1.append(int(i))
    else:
        ls2.append(i)

print(ls1)
print('min=',min(ls1),'max=',max(ls1))
print(ls2)

ls2.reverse()
print(ls2)

