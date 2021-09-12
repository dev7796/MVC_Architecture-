
# declare the employee class
class Employee:
    pass

# create object of the class
emp_1 = Employee()
emp_2 = Employee()

#assign value object to the created instance emp_1.
emp_1.firstName = "Vishal"
emp_1.lastName = "Modi"
emp_1.email = "Vishal.Modi@gmail.com"
emp_1.payment = 10000


#assign value object to the created instance emp_2.
emp_2.firstName = "Harshal"
emp_2.lastName = "Trivedi"
emp_2.email = "Harshal.Trivedi@gmail.com"
emp_2.payment = 20000

# print the result and you will find that each object is stored in different memory location and you will get the result..

print(emp_1.email)
#Vishal.Modi@gmail.com

print(emp_2.email)
#Harshal.Trivedi@gmail.com