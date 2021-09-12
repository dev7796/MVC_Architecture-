# define Python user-defined exceptions

class Error(Exception):
    """Base class for other exceptions"""

    pass


class NumberSmallError(Error):
    """Raised when the input value is too small"""
    pass


class NumberBigError(Error):
    """Raised when the input value is too large"""
    pass


number = 10

while True:
    try:

        i_num = int(input("Enter a number: "))

        if i_num < number:

            raise NumberSmallError

        elif i_num > number:

            raise NumberBigError

        break

    except NumberSmallError:

        print("This value is too small, try again!")

        print()

    except NumberBigError:

        print("This value is too large, try again!")

        print()

print("Congratulations! You guessed it correctly.")

# Sample Output :
# Enter a number: 12
# This value is too large, try again!

# Enter a number: 8
# This value is too small, try again!

# Enter a number: 10
# Congratulations! You guessed it correctly.
