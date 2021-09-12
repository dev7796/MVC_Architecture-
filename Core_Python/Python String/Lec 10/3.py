
# declare the employee class
class Employee:
    def __init__(self,first,last,payment):
        self.first = first
        self.last = last
        self.payment = payment
        self.email = first + "." + last + "@gmail.com"


# create object of the class
emp_1 = Employee("Vishal","Modi",10000)
emp_2 = Employee("Harshal","Trivedi",20000)

# print the result and you will find that each object is stored in different memory location and you will get the result..


print(emp_1.email)
print(emp_2.email)

print(emp_1.payment)
print(emp_2.payment)