class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("sorry, not enough funds")

    def statement(self):
        print("account balance: ${}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):  #these are the arguments they have to enter to open a current account
        super().__init__(name, balance, min_balance = -1000 )#now we have to pass this data to the Account; overdraft of 1000

    def __str__(self):
        return "{}'s current account: balance ${}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s savings account: balance ${}".format(self.name, self.balance)


Z = Current("John", 1000)
Z.deposit(1000)
Z.statement()
Z.withdraw(1000)
Z.statement()
Z.withdraw(1500)
Z.statement()
print(Z)

Y = Savings("Tom", 300)
print(Y)
Y.withdraw(300)
Y.statement()
Y.withdraw(400)
