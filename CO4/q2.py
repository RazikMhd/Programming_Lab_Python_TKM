class Bank:
    accountNo = ""
    name = ""
    typeOfAccount = ""
    balance = 0

    def __init__(self,accountNo,name,typeOfAccount,balance):
       self.accountNo = accountNo
       self.name = name
       self.typeOfAccount = typeOfAccount
       self.balance = balance

    def deposit(self,amount):
       self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount


acc1 = Bank("ACC31323","Laika","Savings",10000)
acc2 = Bank("ACC09932","Megan","Current",8400)

acc1.withdraw(4531)
acc2.deposit(5600)

print(acc1.balance)
print(acc2.balance)