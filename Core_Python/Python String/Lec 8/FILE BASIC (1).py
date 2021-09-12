#file io

#file object = open(file_name,[access_mode])

file = open("1.txt","r")

#access_mode = read,write,append

#Accessing Mode

file = open("1.txt","r+")

"""

r  	==>	reading only.The file pointer is placed at the beginning of the file.This is the default mode.

r+ 	==> both reading and writing.The file pointer placed at the beginning of the file.

rb 	==> reading only in binary format.The file pointer is placed at the beginning of the file.(image read)

rb+ ==> both reading and writing in binary format.The file pointer placed at the beginning of the file.

"""

file = open("1.txt","w+")

'''

w   ==>	writing only.Overwrites the file if the file exists.
		If the file does not exist, creates a new file for writing.

w+  ==>	both writing and reading.Overwrites the existing file if the file exists.
		If the file does not exist, creates a new file for reading and writing.

wb  ==> writing only in binary format.Overwrites the file if the fIle exists.
		If the file does not exist, creates a new file for writing.

wb+ ==> both writing and reading in binary format.Overwrites the existing file if the file exists.
		If the file does not exist, creates a new file for reading and writing.

'''

file = open("1.txt","a+")

'''

a	==>	appending. The file pointer is at the end of the file, if the file exists.
		If the file does not exist, it creates a new file for writing.

a+	==>	both appending and reading.The file pointer is at the end of the file, if the file exists.
		If the file does not exist, it creates a new file for reading and writing.

ab	==>	appending in binary format.The file pointer is at the end of the file if the file exists.
		If the file does not exist, it creates a new file for writing.

ab+	==>	both appending and reading in binary format.The file pointer is at the end of the file, if the file exists.
		If the file does not exist, it creates a new file for reading and writing.

'''

#file object

#read a file
fo = open("foo.txt", "r+")
str = fo.read(10)
position = fo.tell()
#The tell() method tells you the current position(int) within the file

#reposition pointer
fo.seek(0,0)
print ("Read String is : ", str)
fo.close()

#seek(offset,whence)

#offset means character index

#whence means position
#0= begining position
#1= current position
#2= ending position


#write in a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()

