import numpy as np
import re
from itertools import islice

rows=int(input("Please Enter number of Rows: "))
columns=int(input("Please Enter number of Columns: "))
nparray = np.random.random((rows,columns))
print(nparray)


'''def slice_from_string(slice_string):
    slices1=re.split(",|\[|\]",slice_string)
    while ("" in slices1):
        slices1.remove("")
    ls1 = slices1[0].split(':')
    ls2 = slices1[1].split(':')
    while ("" in ls1):
        ls1.remove("")
    while ("" in ls2):
        ls2.remove("")
    for i in range(len(ls1)):
        ls1[i] = int(ls1[i])
    for i in range(len(ls2)):
        ls2[i] = int(ls2[i])
    if len(ls1)>1 and len(ls2)>1:
        split_value=nparray[ls1[0]:ls1[1],ls2[0]:ls2[1]]
        print(split_value)
        print("The shape of the sliced array :", split_value.shape)
    elif len(ls1)<=1 and len(ls2)>1:
        split_value = nparray[0:ls1[0], ls2[0]:ls2[1]]
        print(split_value)
        print("The shape of the sliced array :", split_value.shape)
    elif len(ls1)>1 and len(ls2)<=1:
        split_value = nparray[ls1[0]:ls1[1], 0:ls2[0]]
        print(split_value)
        print("The shape of the sliced array :",split_value.shape)
    else:
        print(nparray)
        print("The shape of the sliced array :", nparray.shape)

no_of_times=int(input("Please enter the no. of times you want to do slicing: "))
for i in range(no_of_times):
    resp = input("Enter 'Y' or 'N' for Slicing: ")
    if resp == 'Y' or resp == 'y':
        silicing_values = (input("Please enter value for silicing: "))
        slice_from_string(silicing_values)
    else:
        if resp == 'N' or resp == 'n':
            break


def mutation(mutate):
    slices1 = re.split(",|\[|\]", mutate)
    while ("" in slices1):
        slices1.remove("")
    for i in range(len(slices1)):
        slices1[i] = int(slices1[i])
    b = np.array(slices1)
    print(nparray[np.arange(len(b)), b])
    # Mutate one element from each row of a using the indices in b
    resp = input("Enter 'Y' or 'N' for Mutating: ")
    if resp == 'Y' or resp == 'y':
        mutate_values = int(input("Please enter value for mutating ONE element in each row: "))
        operation=input("Please enter the operation to be performed for mutation: ")
        if '+' in operation:
            nparray[np.arange(len(b)), b]+=mutate_values
            print(nparray)
        elif '-' in operation:
            nparray[np.arange(len(b)), b] -= mutate_values
            print(nparray)
        elif '*' in operation:
            nparray[np.arange(len(b)), b] *= mutate_values
            print(nparray)
        elif '/' in operation:
            nparray[np.arange(len(b)), b] /= mutate_values
            print(nparray)
        elif '**' in operation:
            nparray[np.arange(len(b)), b] **= mutate_values
            print(nparray)
        elif '//' in operation:
            nparray[np.arange(len(b)), b] //= mutate_values
            print(nparray)
    else:
        if resp == 'N' or resp == 'n':
            print("No input")

mutate=(input("Enter the value of indexes in list form: "))
mutation(mutate)'''

# An example of integer array indexing.
def array_indexing(slice):
    slices1 = re.split(",|\[|\]", slice)
    while ("" in slices1):
        slices1.remove("")
    for i in range(len(slices1)):
        slices1[i] = int(slices1[i])
    l = (int(len(slices1) / 2))
    length_to_split = [l,l]
    Inputt = iter(slices1)
    Output=[list(islice(Inputt, elem))
              for elem in length_to_split]
    print(nparray[Output[0],Output[1]])



slicer=(input("Enter the value of indexes in list form: "))
array_indexing(slicer)

'''def slice_from_string(slice_string):
    slices = slice_string.split(',')
    if len(slices) > 1:
        return [slice_from_string(s.strip()) for s in slices]
    return slice(*[int(x) for x in slice_string.split(':')])'''