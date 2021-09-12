
# declare the employee class

class Employee:

    #variable (5% increment)
    increment_value = 1.05

    def __init__(self,first,last,payment):
        self.first = first
        self.last = last
        self.payment = payment
        self.email = first + "." + last + "@gmail.com"

    
    def fullname(self):
        print('firstname- {} lastname- {}'.format(self.first, self.last))

    def hike_payment(self):
        #self.payment = int(self.payment * 1.05)
        self.payment = int(self.payment * self.increment_value)
        #self.payment = int(self.payment * Employee.increment_value)

# create object of the class
emp_1 = Employee("Vishal","Modi",10000)
emp_2 = Employee("Harshal","Trivedi",20000)

emp_1.fullname()
emp_2.fullname()

print(emp_1.payment)
#10000

emp_1.hike_payment()
print(emp_1.payment)
#10500