Ls = [1, 2, 3, 'a', 'b', 'c', [4, 5, 6, 'd', 'e'], 6, 7, 'f', 'g', [8, 'h', 9, 'i'], ['j']]

for k in Ls[0:6]:
    if (isinstance(k, int)):
        print(k)
    if (isinstance(k, str)):
        print(' ', k)

for r in Ls[6]:
    if (isinstance(r, int)):
        print(r)
    if (isinstance(r, str)):
        print(' ', r)

for k in Ls[7:11]:
    if (isinstance(k, int)):
        print(k)
    if (isinstance(k, str)):
        print(' ', k)

for r in Ls[11]:
    if (isinstance(r, int)):
        print(r)
    if (isinstance(r, str)):
        print(' ', r)

for l in Ls[12]:
    print(' ', l)
