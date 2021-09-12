ls = [0, 8, 4, 12, 2, 12, 4, 9, 10, 11,12 ,1, 3, 5, 13,1, 3, 5, 13, 3,4,5,6,7]
print('My List : ', ls)

ls1 = []
ls2 = [ls1]
ls3=[]

for i in range(len(ls)):

    if len(ls1) == 0:
        ls2[i].append(ls[i])

    elif ls2[-1][-1] <= ls[i]:
        ls2[-1].append(ls[i])

    else:
        ls2.append([ls[i]])

print('Divided into sublist : ', ls2)
'''temp = max(ls2, key=len)
print(temp)
'''
'''
for i in range(1,len(ls2)):
    if len(ls2[i-1])<len(ls2[i]):
        print(ls2[i])
'''

for i in range(len(ls2)):
    ls3.append(len(ls2[i]))
print(ls3)
for j in range(1,len(ls3)):
    if ls3[j-1]<ls3[j]:
        a = ls3[j]

print(ls3.index(a))