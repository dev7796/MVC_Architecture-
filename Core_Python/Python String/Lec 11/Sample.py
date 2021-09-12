Number=int(input("Enter No of person to enter the details= "))
PersonalInfoLs=[]
AccountDetailsLs=[]

class BankInfo():
    def PersonalInfo(self):
        for i in range(Number):
            print(i+1,"Person Bank Information:")
            self.fn=input("Enter First Name= ")
            self.ln=input("Enter Last Name= ")
            self.gender=input("Enter Your Gender= ")
            self.address=input("Enter Your Address= ")
            PersonalInfoLs.append([self.fn,self.ln,self.gender,self.address])
        print("The list of personal information",PersonalInfoLs)

class BankAccount():
    def AccountDetails(self):
        for i in range(Number):
            print(i+1,"Person account Number and Deposit Amount")
            self.acNo=int(input("Enter Account Number= "))
            self.amount=int(input("Enter Amount for Deposit= "))
            AccountDetailsLs.append([self.acNo,self.amount])
        print("The list of account details",AccountDetailsLs[0][1])

class Savings():
    def __init__(self):
        self.Smin_amt=10000
        self.Srate=10

class Current():
    def __init__(self):
        self.Cmin_amt=5000
        self.Crate=5

class Main():
    Bankinfo=BankInfo()
    Bankinfo.PersonalInfo()
    Bankaccount=BankAccount()
    Bankaccount.AccountDetails()
    SavingsAcc=Savings()
    CurrentAcc=Current()
    j=0
    for j in range(len(AccountDetailsLs)):
        choice=input("Enter S for savings / C for Current= ")
        if choice=="S":
            for i in range(3):
                if AccountDetailsLs[j][1]>=SavingsAcc.Smin_amt:
                    print("Account Is Being Created")
                    Duration = int(input("Enter months of Duration= "))
                    interest = (Duration * AccountDetailsLs[j][1] * SavingsAcc.Srate * 0.01)/12
                    print("Annual Interest= ",interest)
                    break
                else:
                    print("Existing balance= ",AccountDetailsLs[j][1])
                    Amount = int(input("Please Add balance as your previous balance is low= "))
                    AccountDetailsLs[j][1]= AccountDetailsLs[j][1] + Amount

        elif choice=="C":
            for i in range(3):
                if AccountDetailsLs[j][1] >= CurrentAcc.Cmin_amt:
                    print("Account Is Being Created")
                    Duration = int(input("Enter months of Duration= "))
                    interest = (Duration * AccountDetailsLs[j][1] * CurrentAcc.Crate * 0.01)/12
                    print("Annual Interest= ", interest)
                    break
                else:
                    print("Existing balance= ",AccountDetailsLs[j][1])
                    Amount = int(input("Please Add balance as your previous balance is low= "))
                    AccountDetailsLs[j][1] = AccountDetailsLs[j][1] + Amount

