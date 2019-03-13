# This program defines a class of bank account with methods for deposits and withdrawals


class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def withdrawal(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("%s, you are overdrawn! Ironically, you will be charged a $35 overdraft fee" % self.name)
            self.balance = self.balance - 50
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount("Alejandro")
b = BankAccount("Bob")
c = BankAccount("Charles")

a.deposit(100)
b.deposit(50)
c.deposit(25)

print("Account A has %d dollars. " % a.balance)
print("Account B has %d dollars. " % b.balance)
print("Account C has %d dollars. " % c.balance)

print("Account holders B and C lost a $30 bet to account holder A. The result:   ")

a.deposit(60)
b.withdrawal(30)
c.withdrawal(30)

print("Account A has %d dollars. " % a.balance)
print("Account B has %d dollars. " % b.balance)
print("Account C has %d dollars. " % c.balance)
    