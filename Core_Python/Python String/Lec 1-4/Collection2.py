Ls = [1, 2, 3, 'a', 'b', 'c', [4, 5, 6, 'd', 'e'], 6, 7, 'f', 'g', [8, 'h', 9, 'i'], ['j']]

for i in Ls:
    if type(i) is list:
        for j in i:
            if type(j) is int:
                print(j)
            if type(j) is str:
                print(' ',j)


    else:
        if type(i) is int:
            print(i)
        if type(i) is str:
            print(' ', i)
