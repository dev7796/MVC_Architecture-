Numofrows = int(input("Enter Number of Rows"))
pattern = input("Enter pattern or number")


def fn1(n, p):
    if pattern.isdigit():
        s = int(p)

        for i in range(0, n):
            for j in range(0, n - i - 1):
                print(end=" ")
            for j in range(0, i + 1):
                print(s, end=" ")
                s = s + 1
            print()
    else:
        for i in range(0, n):
            for j in range(0, n - i - 1):
                print(end=" ")
            for j in range(0, i + 1):
                print(p, end=" ")
            print()


fn1(Numofrows, pattern)
