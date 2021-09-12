n = int(input("enter number of elements"))
lst = []

for i in range(n):

        elements=int(input("enter elements"))

        lst.append(elements)

print(sum(lst))

if sum(lst)%2!=0:
    print("sum is not even therefore cannot be divided")
else:
    print("Your process is in progress")
lst.sort()

left=0
right=0
ls1=[]
ls2=[]
div=len(lst)//2
for k in range(div):
    ls1.append(lst[k])

for k in range(div,len(lst)):
    ls2.append(lst[k])

for j in range(div):
    if sum(ls1)!=sum(ls2):
        ls1.append(ls2[j])
        ls2.pop(j)
    elif sum(ls1)==sum(ls2):
        print("Both the sums are equal")
    else:
        print("It cannot be done")



print(ls1,ls2)