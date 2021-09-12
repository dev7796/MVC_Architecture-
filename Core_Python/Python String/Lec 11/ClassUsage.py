class BankInfo():
    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class BankAccount():
    def __init__(self, acNo, amount):
        self.acNo = acNo
        self.amount = amount

    def chances(self, choice):
        if choice == "S":
            for i in range(3):
                if self.amount >= Savings.Smin_amt:
                    print("Account Is Being Created")
                    print("Existing balance= ", self.amount)
                    break
                else:
                    print("Existing balance= ", self.amount)
                    Amount = int(input("Please Add balance as your previous balance is low= "))
                    self.amount = Amount

        elif choice == "C":
            for i in range(3):
                if self.amount >= Current.Cmin_amt:
                    print("Account Is Being Created")
                    print("Existing balance= ", self.amount)
                    break
                else:
                    print("Existing balance= ", self.amount)
                    Amount = int(input("Please Add balance as your previous balance is low= "))
                    self.amount = Amount
        else:
            print("Please Enter C or S")

    def interest(self, Duration, rate):
        interest = (Duration * self.amount * rate * 0.01) / 12
        print("Annual Interest= ", interest)

class Savings(BankAccount):
    Smin_amt = 10000
    rate = 10


class Current(BankAccount):
    Cmin_amt = 5000
    rate = 5


class Main():
    fn = input("Enter First Name= ")
    ln = input("Enter Last Name= ")
    gender = input("Enter Your Gender= ")
    address = input("Enter Your Address= ")

    acNo = int(input("Enter Account Number= "))
    amount = int(input("Enter Amount for Deposit= "))
    Bankinfo = BankInfo(fn, ln, gender, address)
    SavingsAcc = Savings(acNo, amount)
    CurrentAcc = Current(acNo, amount)

    choice = input("Enter S for savings / C for Current= ")
    if choice == "S" and amount <= SavingsAcc.Smin_amt:
        SavingsAcc.chances(choice)
        Duration = int(input("Enter months of Duration= "))
        SavingsAcc.interest(Duration, SavingsAcc.rate)
    elif choice == "S" and amount >= SavingsAcc.Smin_amt:
        Duration = int(input("Enter months of Duration= "))
        SavingsAcc.interest(Duration, SavingsAcc.rate)
    elif choice == "C" and amount <= CurrentAcc.Cmin_amt:
        CurrentAcc.chances(choice)
        Duration = int(input("Enter months of Duration= "))
        CurrentAcc.interest(Duration, CurrentAcc.rate)
    elif choice == "C" and amount >= CurrentAcc.Cmin_amt:
        Duration = int(input("Enter months of Duration= "))
        CurrentAcc.interest(Duration, CurrentAcc.rate)
    else:
        print("Enter C or S")
