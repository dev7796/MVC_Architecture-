n = int(input("enter number of students"))
dict = {}

for i in range(n):

    dict['s{}'.format(i)] = {
        'rollno': int(input("enter rollno")),
        'name': input("enter name"),
        'marks': int(input("enter marks")),
        'grade': None
    }

for i, j in dict.items():

    for a, b in j.items():

        if a == 'marks':
            if 80 < b < 100:
                j['grade'] = 'A'
            else:
                j['grade'] = 'B'

print(dict)
