import random

class BankInfo:
    def __init__(self, firstname, lastname, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.address = address


class BankAccount:
    def __init__(self, bankInfo, acno, amount):
        self.acno = acno
        self.amount = amount
        self.bankInfo = bankInfo


class Saving(BankAccount):

    minAmount = 10000
    rate = 6
    interest = 0.0

    def validate(self):

        if self.amount >= self.minAmount:
            pass
        else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    pass

                elif i == 3:
                    print("Your 3 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 10000 or Above:"))

    def intrestCalculate(self, months):
        self.months = months
        year = self.months / 12
        self.interest = float((self.amount * self.rate * year) / 100)

    def viewProfie(self):

        print("Complete Profile For Your Saving Account")

        print("FirstName=", self.bankInfo.firstname,
              "\nLastName=", self.bankInfo.lastname,
              "\nGender=", self.bankInfo.gender,
              "\nAddress=", self.bankInfo.address,
              "\nAccount Number=", self.acno,
              "\nAmount=", self.amount,
              "\nRate=", self.rate,
              "\nMonths=", self.months,
              "\nInterest=", self.interest)


class Current(BankAccount):
    minAmount = 5000
    rate = None

    def validate(self):

        if self.amount >= self.minAmount:
            pass

        else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    break

                elif i == 3:
                    print("Your 3 Chance Is Finish!")
                    exit()

                else:
                    self.amount = int(input("Enter Amount 5000 or Above:"))

    def viewProfie(self):

        print("Complete Profile For Your Current Account")

        print("FirstName=", self.bankInfo.firstname,
              "\nLastName=", self.bankInfo.lastname,
              "\nGender=", self.bankInfo.gender,
              "\nAddress=", self.bankInfo.address,
              "\nAccount Number=", self.acno,
              "\nAmount=", self.amount,
              "\nRate=", self.rate,
              "\nNo Interest Available For Current Account !")


class Main:
    def __init__(self):

        f = input("Enter Your First Name:")
        l = input("Enter Your Last Name:")
        g = input("Enter Your Gender:")
        a = input("Enter Your Address:")

        bankInfo = BankInfo(f, l, g, a)

        ac = random.randint(0000000000000, 9999999999999)

        am = int(input("Enter Your Amount:"))

        bankAccount = BankAccount(bankInfo, ac, am)

        print("Select Your Account Type:-1.Saving 2.Current")

        n = int(input("Enter No. 1 or 2:-"))

        if n == 1:

            saving = Saving(bankInfo, ac, am)

            saving.validate()

            months = int(input("Enter Your Months:"))

            saving.intrestCalculate(months)

            saving.viewProfie()

        elif n == 2:

            current = Current(bankInfo, ac, am)

            current.validate()

            months = int(input("Enter Your Month:"))

            current.viewProfie()


objectMain = Main()