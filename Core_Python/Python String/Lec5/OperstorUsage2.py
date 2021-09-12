n = int(input("enter number of elements"))
lst = []
for i in range(n):
    elements = int(input("enter elements"))

    lst.append(elements)
lst.sort()
lst.reverse()
print(lst)
total = sum(lst)
half = total // 2
ls1, ls2 = [], []
if total % 2 == 0 and half >= max(lst):
    for i in lst:
        if sum(ls1) < sum(ls2):
            ls1.append(i)
        else:
            ls2.append(i)
print(sum(ls1))
print(sum(ls2))
