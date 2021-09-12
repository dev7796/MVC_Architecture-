'''from itertools import islice
slices1=[12,2,3,4,5,6]
length_to_split = [int(len(slices1))/2,int(len(slices1))/2]
Inputt = iter(slices1)
Output = [list(islice(Inputt, elem))
    for elem in length_to_split]
print(Output)'''

from itertools import islice

# Input list initialization
Input = [1, 2, 3, 4, 5, 6, ]

# list of length in which we have to split
l=(int(len(Input)/2))
print(type(l))
length_to_split = [l,l]

# Using islice
Inputt = iter(Input)
Output = [list(islice(Inputt, elem))
          for elem in length_to_split]

# Printing Output
print("Initial list is:", Input)
print("Split length list: ", length_to_split)
print("List after splitting", Output)