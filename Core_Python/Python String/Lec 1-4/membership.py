a = 10
b = 20
list = [1, 2, 3, 4, 5]
# in is used for checking multiple values like data structures and advantage is not to use for loop
if a in list:
    print("answer 1 true")
else:
    print("answer 1 false")

if b not in list:
    print("answer 2 - false")

else:
    print("answer 2 - true ")

a = 2
if a in list:
    print("answer 3 - true")
else:
    print("answer 3 - false ")
