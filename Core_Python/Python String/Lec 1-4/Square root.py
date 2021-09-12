num = input("Enter the number for its square root")
print(len(num))
ls1=[]
ls2=[]

if len(num)%2==0:
    ls=list(num)
    ls1.append(ls[2])
    ls1.append(ls[3])
    print(ls1)
    ls2.append(ls[0])
    ls2.append(ls[1])
    stringg=' '.join([str(elem) for elem in ls2])
    
