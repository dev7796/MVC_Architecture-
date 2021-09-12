Nooflines=int(input("Enter Number of Lines"))
file = open("1.txt", "w+")

def writing(lines):
    for i in range(lines):
        file.write(input("Enter lines")+'\n');
    print("Number of lines =",lines)

writing(Nooflines)
file.seek(0,0)
position=file.tell()
print("Current Position of cursor",position)
i=0
def reading():
    str=file.read()
    print(str)
    e = list(str)
    print("Total Number of Characters = ", len(e))

    c=str.split()
    d=list(c)
    print(d)
    print("Total number of words =",len(d))

reading()

file.close()