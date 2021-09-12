#Task 1 pattern
Numofrows = int(input("Enter Number of Rows"))

#print(Numofrows)
for i in range(0,Numofrows):
    for j in range(0,Numofrows-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


'''
for i in range(0,Numofrows):
    for j in range(0,):
        print(end=" ")
    for j in range(0,i+1):
        print(i,end=" ")
    print()
'''


z = 1
while z<7:
    for i in range(0,Numofrows):
        for j in range(0,Numofrows-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print(z,end=" ")
            z = z+1
        print()


space = (Numofrows * 2) - 2
for i in range(0,Numofrows):
    for j in range(0,space):
        print(end=" ")
    space = space - 2
    for j in range(0,i+1):
        print("*  ",end=" ")
    print()

space = 2
for i in range(i,0,-1):
    for j in range(0,space):
        print(end=" ")
    space = space + 2
    for j in range(0,i):
        print("*  ",end=" ")
    i = i - 1
    print()





