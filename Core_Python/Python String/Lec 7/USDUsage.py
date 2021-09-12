Nooflist = int(input("Enter number of lists"))
ls = []
ls1 = []
ls2 = []
ls3 = []


def fn(*ls):
    if len(ls) == 1:
        for var in ls:
            print(var)

    if len(ls) == 2:
        for var in ls:
            print(var)
        for i in ls[1]:
            ls[0].append(i)
        print("Concated list", ls[0])
        ls[0].sort()
        print("Sorted List", ls[0])

    if len(ls) == 3:
        for var in ls:
            print(var)
        for i in ls[1]:
            ls[0].append(i)

        for j in ls[2]:
            ls[0].append(j)

        print("Concated list", ls[0])
        ls[0].sort()
        print("Sorted list", ls[0])
        print("maximum of this list", max(ls[0]))
        print("minimum of this list", min(ls[0]))


if Nooflist == 1:
    Elements = int(input("Enter No. of Elements"))
    for j in range(Elements):
        Elements1 = input("Enter elements")
        ls1.append(Elements1)
    fn(ls1)

elif Nooflist == 2:
    Elements = int(input("Enter No. of Elements"))
    for j in range(Elements):
        Elements1 = int(input("Enter elements"))
        ls1.append(Elements1)

    Elements1 = int(input("Enter No. of Elements"))
    for j in range(Elements1):
        Elements1 = int(input("Enter elements"))
        ls2.append(Elements1)
    fn(ls1, ls2)

else:
    Elements = int(input("Enter No. of Elements"))
    for j in range(Elements):
        Elements1 = input("Enter elements")
        ls.append(Elements1)
    Elements1 = int(input("Enter No. of Elements"))
    for j in range(Elements1):
        Elements1 = input("Enter elements")
        ls1.append(Elements1)
    Elements2 = int(input("Enter No. of Elements"))
    for j in range(Elements2):
        Elements2 = input("Enter elements")
        ls2.append(Elements2)
    fn(ls, ls1, ls2)
