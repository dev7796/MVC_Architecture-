# declare the employee class
class Employee:
	"""this is desc of employee class"""
	pass
	
def myfunction():
	"""this is desc of my function"""
	print("this is my function")

# create object of the class.
emp_1 = Employee()
emp_2 = Employee()

print(Employee.__doc__)
#this is desc of employee class

print(myfunction.__doc__)
#this is desc of my function


# print the result and you will find that each object is stored in different memory location.

print(emp_1)
#<__main__.Employee object at 0x00000294F1016B70>

print(emp_2)
#<__main__.Employee object at 0x00000294F1016EF0>
