try:

    a = [1, 2, 3, 4]

    print('Second Element : ', a[2])

    print('Fourth Element : ', a[4])

    print('Zero Element   : ', a[0])

except IndexError:

    print('Index Error Occured.')

try:

    n = input(int('Enter Integer : '))
    print(n)

except ValueError:

    print('Value Error Occurred.')

try:
    a = 10
    b = 0
    a / b

except ArithmeticError:

    print('Arithmetic Error Occurred')

try:
    i = 1
    f = 3.0 ** i
    for i in range(100):
        print(i, f)
        f = f ** 2

except OverflowError:

    print("Overflow Error Occurred")

try:

    from sortingfile import sorting2

except ImportError:

    print('Import Error Occured')


def temp_convert(var):
    try:

        return int(var)

    except ValueError:

        print("The argument does not contain numbers", var)


temp_convert("xyz")

try:

    fh = open("testfile", "r")

    try:

        fh.write("This is my test file for exception handling!!")

    finally:

        print("File Close")
        fh.close()

except IOError:

    print("Error: can\'t find file or read data")

try:

    fh = open("testfile1", "w")

    fh.write("This is my test file for exception handling!!")

except IOError:

    print("Error: can\'t find file or read data")

else:

    print("File Close")
    fh.close()

'''

SyntaxErrors-IndentationErrors get raised when the file/code is parsed, not when that line of code is executed.
If the syntax is wrong at a single point in the code,
the parser can't continue so all code after that line is un-parseable.

In other words, you can only catch syntax errors when python is trying to parse something.
This includes exec, eval, import:

	for i range(0,10,1):
			  ^
SyntaxError: invalid syntax


	for i in range(0, 10, 1):

print i
	   ^
IndentationError: expected an indented block

'''
