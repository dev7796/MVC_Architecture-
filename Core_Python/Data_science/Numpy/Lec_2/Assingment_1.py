import numpy as np

# Creating a NumPy Array
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = float)

#place Holders
np.zeros((3,4)) #Create an array of zeros
np.ones((2,3,4),dtype=np.int16) #Create an array of ones
d = np.arange(10,25,5) #Create an array of evenly spaced values (step value)
print("This is linespace: ",np.linspace(0,2,9)) #Create an array of evenly spaced values (number of samples)
e = np.full((2,2),7) #Create a constant array
f = np.eye(2) #Create a 2X2 identity matrix
np.random.random((2,2)) #Create an array with random values
print("This is Empty: ",np.empty((3,2)))
print("This is D: ",d)
print("This is E: ",e)
print("This is F: ",f)

#Saving and loading on the disk
np.save('my_array', a)
np.savez('array.npz', a, b)
#print("-----------:",np.load('my_array'))


print(np.loadtxt('myfile.txt'))
np.genfromtxt("my_file.csv", delimiter=',')
np.savetxt("myarray.txt", a, delimiter=" ") #doubt

np.int64 #Signed 64-bit integer types
np.float32 #Standard double-precision floating point
np.complex #Complex numbers represented by 128 floats
np.bool #Boolean type storing TRUE and FALSE values
np.object #Python object type
np.string_ #Fixed-length string type
np.unicode_ #Fixed-length unicode type

#Inspecting Your Array
print(a.shape) #Array dimensions
print(len(a)) #Length of array
print(b.ndim) #Number of array dimensions
print(b.size) #Number of array elements
print(b.dtype) #Data type of array elements
print(b.dtype.name) #Name of data type
print(b.astype(int)) #Convert an array to a different type

#Asing for Help
print(np.info(np.ndarray.dtype))

#Mathematics

print(a - b) #Subtraction
print(np.subtract(a,b)) #Subtraction
print(b + a) #Addition
print(np.add(b,a)) #Addition
print(a / b) #Division
print(np.divide(a,b)) #Division
print(a * b) #Multiplication
print(np.multiply(a,b)) #Multiplication
print("exp: ", np.exp(b)) #Exponentiation in the form of e^x
print("sqrt: ",np.sqrt(b)) #Square root
print("sin: ",np.sin(a)) #Print sines of an array
print("cos:",np.cos(b)) #Element-wise cosine
print('log: ',np.log(a)) #Element-wise natural logarithm
print('dot: ',e.dot(f)) #Dot product

#Array wise comparision

print('Comapare:',a == b) #Element-wise comparison
print('Compare:',a < 2) #Element-wise comparison
print('Compare:',np.array_equal(a, b)) #Array-wise comparison

#Aggregate

print("Sum: ",a.sum()) #Array-wise sum
print("min:",a.min())#Array-wise minimum value
print("max:",b.max(axis=0)) #Maximum value of an array row
print("cumsum:",b.cumsum(axis=1)) #Cumulative sum of the elements
print("mean:",a.mean()) #Mean
print("median:",np.median(a,axis=0)) #Median '''Sytanx chaged'''
print("corrcoef:",np.corrcoef(a)) #Correlation coefficient '''change of 1 is seen in correlation'''
print("std:",np.std(b)) #Standard deviation

#copying arrays
h = a.view() #Create a view of the array with the same data
print("this is view:",h)#only dimentions can be chnaged
print("this is copy:",np.copy(a)) #Create a copy of the array of new without affect old
h = a.copy() #Create a deep copy of the array
print("This is deep copy",h)#along with dimentions, values can be chnaged too of the new array.
'''When the contents are physically stored in another location, it is called Copy. 
If on the other hand, a different view of the same memory content is provided, we call it as View'''

#Array Manipulation
#NumPy Arrays
#Transposing Array
i = np.transpose(b) #Permute array dimensions
print("Transpose:",i.T) #Permute array dimensions
#Changing Array Shape
print("Flatten:",b.ravel())#Flatten the array
print("Reshape:",b.reshape(3,-2)) #Reshape, but don’t change data

# Adding/Removing Elements
print("resize:",h.resize((2,6)) )#Return a new array with shape (2,6)
print("Append:",np.append(h,d)) #Append items to an array
print("insert:",np.insert(a, 1, 5)) #Insert items in an array
print("delete:",np.delete(a,[1])) #Delete items from an array

# Combining Arrays
print("Concate:",np.concatenate((a,d),axis=0)) #Concatenate arrays
print("stack:",np.vstack((a,b))) #Stack arrays vertically (row-wise)

print("stack row::",np.r_[e,f]) #Stack arrays vertically (row-wise)
print("Stack column:",np.hstack((e,f))) #Stack arrays horizontally (column-wise)

print("Column stack combine 2 array:",np.column_stack((a,d)) )#Create stacked column-wise arrays
print("2nd method:",np.c_[a,d]) #Create stacked column-wise arrays

#Splitting Arrays
print("split horrizontal at 3rd:",np.hsplit(a,3))#Split the array horizontally at the 3rd
print("split vertical at the 3rd:",np.vsplit(b,2)) #Split the array vertically at the 2nd index

#boolean indexing
print("C....:",c[1,...]) #Same as [1,:,:]

print("reverse a:",a[ : :-1] )#Reversed array a

#Boolean Indexing
print("a,2",a[a<2]) #Select elements from a less than 2


#Fancy Indexing
print("Fancy b",b[[1, 0, 1, 0],[0, 1, 2, 0]]) #Select elements (1,0),(0,1),(1,2) and (0,0)

print("subset:",b[[1, 0, 1, 0]][:,[0,1,2,0]]) #Select a subset of the matrix’s rows and columns
#first the output of rows is difiend and in second the pattern
