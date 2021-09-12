n = int(input("enter number of elements"))
lst = []

for i in range(n):
    elements = int(input("enter elements"))

    lst.append(elements)
k=1
ls1=[lst[0]]
for j in range(len(lst)):
    if lst[j-1]<lst[j]:
        ls1[len(ls1)-1].append(lst[j])
    else:
        ls1.append(lst[j])
print(ls1)

