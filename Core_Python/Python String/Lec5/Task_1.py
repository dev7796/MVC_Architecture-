ls = [0, 8, 4, 12, 2, 12, 4, 9, 1, 3, 5, 13, 3]
# ls=[1,2,3,4]
# ls = [1, 2, 7]

ls1 = []
ls2 = []

ls.sort(reverse=True)

print(ls)

total = sum(ls)

print(total)

half = total // 2

print(half)

if total % 2 == 0 and half > max(ls):

    for i in ls:
        if sum(ls1) < sum(ls2):

            ls1.append(i)
        else:
            ls2.append(i)

    print(ls1)
    print(ls2)

    print(sum(ls1))
    print(sum(ls1))

else:
    print("Not Possible For This List !")
