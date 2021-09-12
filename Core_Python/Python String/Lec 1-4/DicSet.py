
p = input("enter number of students")
q = int(p)

dict={}

for n in range(q):
    dict['name{}'.format(n)] = input("enter name of the student")
    dict['marks{}'.format(n)] = int(input("enter marks"))
    dict['rollno{}'.format(n)] = int(input("enter rollno"))


print(dict)
'''for k,v in dict.items():
    print(k,v)
   '''


