n = int(input("enter number of elements"))
lst = []

for i in range(n):
    elements = int(input("enter elements"))

    lst.append(elements)

ls1 = [[lst[0]]]
for i in range(1,len(lst)):
    if lst[i - 1] < lst[i]:
        ls1[len(ls1) - 1].append(lst[i])
    else:
        ls1.append([lst[i]])
print(ls1)

